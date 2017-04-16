#!/usr/bin/env python3
import typing
import re
import os.path
import enum
import json
import urllib
import argparse
import lxml.html
import requests
import lxml.etree

HOME = os.path.expanduser("~")
USERNAME = "adwin_"  # type: str
CONTEST_DIR = os.path.join(HOME, "algo_competitions")  # type: str


class Example:
    def __init__(self, _input: str, output: str):
        """
        sometimes input/output is missing trailing \n
        """
        self.input = _input
        self.output = output

    def __str__(self):
        return "input:\n"+self.input+"output:\n"+self.output

    @staticmethod
    def get_example_text(node: lxml.html.HtmlElement)->str:
        s = node.text
        if s is None:
            s = ''
        for child in node:
            s += lxml.etree.tostring(child, encoding='unicode')
        return s.replace("<br/>", "\n")


class Problem:
    PROBLEM_LINK_PATTERN = re.compile(".*/contest/\d+/problem/(.+?)")

    def __init__(self, problem_link: str, examples: typing.List[Example]):
        self.problem_link = problem_link
        self.problem_name = self._get_problem_name(problem_link)
        self.examples = examples

    def __str__(self):
        problem_as_str = self.problem_link+"\n"
        for example in self.examples:
            problem_as_str += str(example)
        return problem_as_str

    @staticmethod
    def _get_problem_name(problem_link: str):
        found = Problem.PROBLEM_LINK_PATTERN.match(problem_link)
        assert found
        return found.group(1)

    def write(self, contest_directory: str):
        problem_directory = os.path.join(contest_directory, self.problem_name)
        if not os.path.isdir(problem_directory):
            os.makedirs(problem_directory)
        for index, example in enumerate(self.examples, start=1):
            input_path = os.path.join(problem_directory, "in%s.txt" % index)
            output_path = os.path.join(problem_directory, "expected%s.txt" % index)
            with open(input_path, "w+") as input_file:
                input_file.write(example.input)
            with open(output_path, "w+") as output_file:
                output_file.write(example.output)


class Division(enum.IntEnum):
    ONE = 1
    TWO = 2


class Codeforces:
    CONTEST_GENERIC_URL = "http://codeforces.com/contest/%s"
    CONTEST_LINK_PATTERN = re.compile("^(http://)?(www\.)?codeforces.com/contest/(\d+?)(/+.*)?$")

    class NoContestRunning(Exception):
        pass

    @staticmethod
    def get_contest_id_from_contest_link(contest_link: str)->str:
        return Codeforces.CONTEST_LINK_PATTERN.match(contest_link).group(3)

    @staticmethod
    def _get_user_rating(handle: str)->int:
        response = requests.get("http://codeforces.com/api/user.info?%s" % (urllib.parse.urlencode({"handles": handle})))
        assert response.status_code == 200,\
            "Could not fetch user rating using Codeforces API - response status %s" % response.status_code
        api_info = json.loads(response.content.decode("utf-8"))
        results = api_info.get("result")  # type: typing.List[typing.Dict[str,typing.Any]]
        for user_info in results:
            if not user_info.get("handle") == handle:
                continue
            else:
                return user_info.get("rating")
        raise NotImplementedError("No info about user in the response. Response: %s" % api_info)

    @staticmethod
    def _get_user_division()->Division:
        user_rating = Codeforces._get_user_rating(USERNAME)
        if user_rating <= 1900:
            return Division.TWO
        else:
            return Division.ONE

    @staticmethod
    def get_problem(link: str) -> Problem:
        page = requests.get(link)
        assert page.status_code == 200, "Page %s is not accessible - request status code %s" % (link, page.status_code)
        tree = lxml.html.fromstring(page.content)
        inputs = []  # type: typing.List[str]
        outputs = []  # type: typing.List[str]
        for test_div in tree.xpath("//div[@class='sample-test']"):
            for input_div in test_div.xpath("//div[@class='input']"):
                pre = input_div.xpath("pre")[0]
                inputs.append(Example.get_example_text(pre))
            for output_div in test_div.xpath("//div[@class='output']"):
                pre = output_div.xpath("pre")[0]
                outputs.append(Example.get_example_text(pre))
        assert len(inputs) == len(outputs)
        return Problem(problem_link=link,
                       examples=[Example(inputs[index], outputs[index]) for index in range(len(inputs))])

    @staticmethod
    def get_problems(contest_link: str) -> typing.List[Problem]:
        contest = requests.get(contest_link)
        assert contest.status_code == 200,\
            "Could not fetch contest page: %s status code: %s" % (contest_link, contest.status_code)
        tree = lxml.html.fromstring(contest.content)
        tree.make_links_absolute(contest_link)
        problem_links = set()
        for element, attribute, link, pos in tree.iterlinks():
            if Problem.PROBLEM_LINK_PATTERN.match(link):
                problem_links.add(link)
        return [Codeforces.get_problem(link) for link in problem_links]

    @staticmethod
    def get_currently_running_contest()->str:
        CONTESTS_URL = "http://codeforces.com/contests/"
        contests_page = requests.get(CONTESTS_URL)
        assert contests_page.status_code == 200, "Could not open the contest page"
        user_division = Codeforces._get_user_division()
        print("Downloading division %s" % user_division.value)
        tree = lxml.html.fromstring(contests_page.content)
        tree.make_links_absolute(CONTESTS_URL)
        for contest in tree.xpath("//tr[@data-contestid]"):
            contest_id = contest.get("data-contestid")  # type: str
            if "Div. %s" % user_division.value not in lxml.html.tostring(contest, encoding="unicode"):
                continue
            red_enter_links = contest.xpath('.//a[@class="red-link"]')  # type: typing.List[lxml.html.HtmlElement]
            for red_enter_link in red_enter_links:
                contest_link = Codeforces._extract_contest_link(red_enter_link.get("href"))
                assert Codeforces.get_contest_id_from_contest_link(contest_link) == contest_id
                return contest_link
        else:
            raise Codeforces.NoContestRunning(
                "No contest for your division is running. "
                "Please use the --link option to specify the direct link to the contest.")

    @staticmethod
    def _extract_contest_link(contest_link: str)->str:
        """in case sb provides http://codeforces.com/contest/779/problem/D instead of http://codeforces.com/contest/779"""
        found = Codeforces.CONTEST_LINK_PATTERN.match(contest_link)
        assert found, "Invalid contest link: %s - link did not match the pattern: %s" % \
                      (contest_link, Codeforces.CONTEST_LINK_PATTERN.pattern)
        for i in found.groups():
            if i == "http://" or i == "www." or not i:
                continue
            else:
                round_id = i
                break
        return Codeforces.CONTEST_GENERIC_URL % round_id

    @staticmethod
    def download_examples(contest_link: str = None, contest_name: str = None, contest_full_path: str = None):
        assert contest_name or contest_full_path
        if not contest_link:
            contest_link = Codeforces.get_currently_running_contest()
        else:
            contest_link = Codeforces._extract_contest_link(contest_link)
        problems = Codeforces.get_problems(contest_link)
        assert problems
        if not contest_full_path:
            contest_full_path = os.path.join(CONTEST_DIR, contest_name)
        print("Downloading examples from: %s to %s" % (contest_link, contest_full_path))
        for problem in problems:
            problem.write(contest_full_path)


def handle_username_change(new_username: str):
    raise NotImplementedError()
def handle_contest_directory_change(new_contest_directory: str):
    raise NotImplementedError()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="examples will be written to /tmp/codeforces/")
    parser.add_argument("-n", "--contest-name", help="contest name - for example ct403 for Codeforces Round #403")
    parser.add_argument("-d", "--contest-dir", help="path to contest directory to save examples in")
    parser.add_argument("-l", "--link", help="link to the contest (or any of the examples in the contest) - "
                                             "for example: http://codeforces.com/contest/779")
    parser.add_argument("--set-username",
                        help="your username - used to deduce the contest you are participating in (when not using the --link flag),"
                             " when there are two concurrent contests for div 1 and div 2")
    parser.add_argument("--set-contest-dir",
                        help="set contest directory - examples are saved in $CONTEST_DIR/$PROBLEM_NAME/in(ID).txt")
    args = parser.parse_args()
    Codeforces.download_examples(
        contest_link=args.link,
        contest_name=args.contest_name,
        contest_full_path=args.contest_dir if not args.demo else "/tmp/codeforces/"
    )

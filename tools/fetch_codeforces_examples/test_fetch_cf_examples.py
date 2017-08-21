import unittest
import unittest.mock

import pytest
import fetch_cf_examples


class TestCodeforces(unittest.TestCase):
    def test_extract_contest_link_validates_valid_link_correctly(self):
        link = "http://codeforces.com/contest/785"
        self.assertEqual(fetch_cf_examples.Codeforces._extract_contest_link(link), link)

    def test_extract_contest_link_removes_not_important_suffix(self):
        problem_link = "http://codeforces.com/contest/785/problem/A"
        contest_link = "http://codeforces.com/contest/785"
        self.assertEqual(fetch_cf_examples.Codeforces._extract_contest_link(problem_link), contest_link)

    def test_extract_contest_link_removes_not_important_stuff_from_the_link(self):
        some_link = "http://codeforces.com/contest/785/yolo"
        contest_link = "http://codeforces.com/contest/785"
        self.assertEqual(fetch_cf_examples.Codeforces._extract_contest_link(some_link), contest_link)

    def test_extract_contest_link_does_not_accept_wrong_contest_links(self):
        invalid_contest_link = "http://www.codeforces.com/contest/1a"
        self.assertRaises(AssertionError, fetch_cf_examples.Codeforces._extract_contest_link, invalid_contest_link)

    def test_get_contest_id_out_of_link_with_http(self):
        self.assertEqual(
            fetch_cf_examples.Codeforces.CONTEST_LINK_PATTERN.match("http://codeforces.com/contest/789").group(3),
            "789")

    def test_get_contest_id_out_of_link_without_http(self):
        self.assertEqual(
            fetch_cf_examples.Codeforces.CONTEST_LINK_PATTERN.match("codeforces.com/contest/789").group(3),
            "789")

    def test_get_contest_id_out_of_link_with_www(self):
        self.assertEqual(
            fetch_cf_examples.Codeforces.CONTEST_LINK_PATTERN.match("www.codeforces.com/contest/789").group(3),
            "789")

    @unittest.mock.patch("requests.get")
    def test_get_problem(self, requests_get_mock: unittest.mock.MagicMock):
        page = unittest.mock.MagicMock()
        page.status_code = 200
        inputs = ["5 4\n3 2", "111 222\n555 2 -1 -7", "999 221\n22 1 0\n5 5 5"]
        outpus = ["1", "2\n", "2\n1 5 8\n2 5 6"]
        content = """
        <div class="sample-test">
            <div class="input">
                <div class="title">Input</div>
                <pre>{0}</pre>
            </div>
            <div class="output">
                <div class="title">Output</div>
                <pre>{1}</pre>
            </div>
            <div class="input">
                <div class="title">Input</div>
                <pre>{2}</pre>
            </div>
            <div class="output">
                <div class="title">Output</div>
                <pre>{3}</pre>
            </div>
            <div class="input">
                <div class="title">Input</div>
                <pre>{4}</pre>
            </div>
            <div class="output">
                <div class="title">Output</div>
                <pre>{5}</pre>
            </div>
        </div>
        """.format(*[pre_contents.replace("\n", "<br>") for input_output_pair in zip(inputs, outpus)
                                                        for pre_contents in input_output_pair])
        page.content = content.encode()
        requests_get_mock.return_value = page

        link = "http://codeforces.com/contest/839/problem/A"
        problem = fetch_cf_examples.Codeforces.get_problem(link)
        assert link == problem.problem_link
        assert len(problem.examples) == 3
        assert problem.examples == [
            fetch_cf_examples.Example(inputs[0], outpus[0]),
            fetch_cf_examples.Example(inputs[1], outpus[1]),
            fetch_cf_examples.Example(inputs[2], outpus[2])]


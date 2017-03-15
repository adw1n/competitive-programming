import unittest
import fetch_cf_examples
class TestCodeforces(unittest.TestCase):
    def test_extract_contest_link_validates_valid_link_correctly(self):
        link="http://codeforces.com/contest/785"
        self.assertEqual(fetch_cf_examples.Codeforces._extract_contest_link("http://codeforces.com/contest/785"),link)
    def test_extract_contest_link_removes_not_important_suffix(self):
        problem_link="http://codeforces.com/contest/785/problem/A"
        contest_link = "http://codeforces.com/contest/785"
        self.assertEqual(fetch_cf_examples.Codeforces._extract_contest_link(problem_link),contest_link)
    def test_extract_contest_link_removes_not_important_stuff_from_the_link(self):
        some_link="http://codeforces.com/contest/785/yolo"
        contest_link = "http://codeforces.com/contest/785"
        self.assertEqual(fetch_cf_examples.Codeforces._extract_contest_link(some_link),contest_link)
    def test_extract_contest_link_does_not_accept_wrong_contest_links(self):
        invalid_contest_link="http://www.codeforces.com/contest/1a"
        self.assertRaises(AssertionError,fetch_cf_examples.Codeforces._extract_contest_link,invalid_contest_link)
if __name__ == '__main__':
    unittest.main()
import unittest
from assignment4 import get_repo_info

class TestGetRepoInfo(unittest.TestCase):
    def test(self):
        self.assertEqual(get_repo_info(" "), {}, 'Empty string is invalid')
    def test1(self):
        self.assertEqual(get_repo_info(123), {}, 'Invalid input')  
        self.assertEqual(get_repo_info("..."), {}, 'Invalid input')  
    def test2(self):
        self.assertEqual(get_repo_info("wrong_id"), {}, 'Wrong id is invalid')
        self.assertEqual(get_repo_info("!@#"), {}, 'Special characters in id are invalid')
    def test3(self):
        self.assertEqual(get_repo_info("hellohii"), {}, 'User has no repositories')

if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
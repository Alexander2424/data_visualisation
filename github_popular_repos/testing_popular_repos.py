import unittest
from matplotlib.pyplot import get
import requests
from random import randint

def api_call(language):
    """Return API call return code"""
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    r = requests.get(url)
    return r

class ReturnCodeTestCase(unittest.TestCase):
    """Test for popular_repos.py"""

    def setUp(self):
        languages = ["Python", "JavaScript", "Ruby", "C", "Java", "Haskell", "Go"]
        self.language = languages[randint(0,6)]
        print("\n\nLanguage tested: " + self.language)
        self.code = api_call(self.language)

    def test_return_code(self):
        # Test for return code (200)
        status = self.code.status_code
        # print("\nReturn code: " + status + "\n")
        self.assertEqual(status, 200)

    def test_min_reps(self):
        # Test that at least 1000 repositories exist for the language
        response_dict = self.code.json()
        total_reps = response_dict['total_count']
        # print("\nTotal repositories found: " + str(total_reps) + "\n")
        self.assertTrue(total_reps > 1000)

    def test_total_reps(self):
        # Test that total number of detailed repositories returned is 30
        response_dict = self.code.json()
        repo_dicts = response_dict['items']
        total_items = len(repo_dicts)
        # print("\nRepositories with detail returned: " + total_items + "\n")
        self.assertEqual(total_items, 30)

if __name__ == '__main__':
    unittest.main()
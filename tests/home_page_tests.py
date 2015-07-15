import unittest

from selenium import webdriver

from pages.home_page import HomePage


class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.jasminenoack.com/flallo")

    def test_home_page_title(self):
        home = HomePage(self.driver)
        title = home.driver_title()
        assert title == "Flallo", "Title is not as expected: {}".format(title)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

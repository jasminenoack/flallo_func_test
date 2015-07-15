import unittest

from selenium import webdriver

from pages.home_page import HomePage


class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.jasminenoack.com/flallo")

    def test_home_page_title(self):
        home = HomePage(self.driver)
        title = home.driver_title
        assert title == "Flallo"

    def test_home_page_header(self):
        home = HomePage(self.driver)
        header = home.page_header
        assert header == "Welcome to Flallo"

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

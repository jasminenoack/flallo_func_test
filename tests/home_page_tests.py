import unittest

from selenium import webdriver

from pages.home_page import HomePage


class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        # self.driver.get("https://www.jasminenoack.com/flallo")
        self.driver.get("file:///Users/jasminenoack/Desktop/flallo/flallo_frontend/index.html")

    def test_home_page_title(self):
        home = HomePage(self.driver)
        title = home.driver_title
        assert title == "Flallo"

    def test_home_page_header(self):
        home = HomePage(self.driver)
        header = home.page_header
        assert header == "Welcome to Flallo"

    def test_displays_tasks(self):
        home = HomePage(self.driver)
        cards = home.task_cards
        assert len(cards) > 0

    def test_displays_tasks_sorted_by_status(self):
        home = HomePage(self.driver)
        card_status_order = home.cards_status_order
        assert card_status_order == ["In progress", "Queued", "Backlog", "Resolved"]

    def test_displays_tasks_within_status_most_recent_first(self):
        home = HomePage(self.driver)
        in_progress_cards = home.in_progress_cards_dates
        assert in_progress_cards == sorted(in_progress_cards)
        queued_cards = home.queued_cards_dates
        assert queued_cards == sorted(queued_cards)
        backlog_cards = home.backlog_cards_dates
        assert backlog_cards == sorted(backlog_cards)
        resolved_cards = home.resolved_cards_dates
        assert resolved_cards == sorted(resolved_cards)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

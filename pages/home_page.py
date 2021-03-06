from pages.base_page import BasePage
from selenium.webdriver.common.by import By


TASK_CARDS = (By.CLASS_NAME, "task_card")


class HomePage(BasePage):
    @property
    def task_cards(self):
        tasks = self.driver.find_elements(*TASK_CARDS)
        return [task.text for task in tasks]

    @property
    def cards_status_order(self):
        tasks = self.driver.find_elements(*TASK_CARDS)
        statuses = [task.get_attribute("data-status") for task in tasks]
        return [
            status
            for i, status in enumerate(statuses)
            if status > 0 and status != statuses[i - 1]
        ]

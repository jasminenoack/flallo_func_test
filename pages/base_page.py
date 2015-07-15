from selenium.webdriver.common.by import By


PAGE_HEADER_LOCATOR = (By.ID, "page_header")


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def driver_title(self):
        return self.driver.title

    @property
    def page_header(self):
        return self.driver.find_element(*PAGE_HEADER_LOCATOR).text

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def driver_title(self):
        return self.driver.title

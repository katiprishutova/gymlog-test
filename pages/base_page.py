from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, *args):
        return self.driver.find_element(*args)

    def find_all(self, *args):
        return self.driver.find_elements(*args)

    @staticmethod
    def move_between_windows(driver, url):
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.current_url == url:
                break
        return driver




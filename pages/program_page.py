from pages.base_page import BasePage
from selenium.webdriver.common.by import By

params = (By.XPATH, '//div[@class="params"]/div')


class ProgramPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def return_params(self):
        return self.find_all(params)

    def return_list_params(self):
        return [param.text for param in self.find_all(*params)]

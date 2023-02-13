from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

my_programs_button = (By.XPATH, '//i[@class="fa fa-trophy"]//ancestor::a[1]')
new_program_button = (By.XPATH, '//a[@class="btn btn-success pull-right"]')
delete_button = '//a[@class="btn btn-xs btn-danger"][1]'


class MyProgramsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_my_programs_from_start(self):
        self.find(*my_programs_button).click()

    def click_new_program(self):
        self.find(*new_program_button).click()

    def is_private(self, name):
        return self.find(By.XPATH, f'//a[text()="{name}"]//ancestor::tr[1]/td[3]').text == 'приватная'

    def delete_program(self, driver):
        name = self.find(By.XPATH, delete_button).text
        self.find(By.XPATH, delete_button).click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        return name

    def is_program_exists(self, name):
        return len(self.find_all(By.XPATH, f'//a[text()="{name}"]')) > 0


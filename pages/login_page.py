from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK_LOGIN_PAGE = "https://gymlog.ru/profile/login/"

login_field = (By.ID, "email")
password_field = (By.ID, "password")
enter_button = (By.XPATH, '//button[@class = "btn btn-primary pull-right"]')
exit_button = (By.CLASS_NAME, "last")


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(LINK_LOGIN_PAGE)

    def login(self, driver, login, password):
        self.find(*login_field).send_keys(login)
        self.find(*password_field).send_keys(password)
        self.find(*enter_button).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(self.find(*exit_button)))

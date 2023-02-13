from pages.base_page import BasePage
from selenium.webdriver.common.by import By

LINK_CREATE_NEW_PROGRAM = "https://gymlog.ru/program/create/"
name_field = (By.XPATH, '//input[@id="field_name_u"]')
description = (By.XPATH, '//input[@id="field_name_u"]')
checkbox_public = (By.XPATH, '//input[@id="field_is_public"]')
save_button = (By.XPATH, '//button[@class="btn btn-primary pull-right"]')
select_categories = (By.XPATH, '//ul[@class="select2-selection__rendered"]')
categories = (By.XPATH, '//li[@class="select2-results__option"][1]')


class CreateNewProgramPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(LINK_CREATE_NEW_PROGRAM)

    def click_save_button(self):
        self.find(*save_button).click()

    def fill_name_field(self, text):
        self.find(*name_field).send_keys(text)

    def fill_description(self, text):
        self.find(*description).send_keys(text)

    def fill_categories(self):
        self.find(*select_categories).click()
        if len(self.find_all(*categories)) > 0:
            element = self.find(*categories)
            name = element.text
            element.click()
            return name

    def mark_checkbox_public(self):
        self.find(*checkbox_public).click()

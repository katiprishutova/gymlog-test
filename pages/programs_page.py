from pages.base_page import BasePage
from selenium.webdriver.common.by import By

LINK_PROGRAMS = 'https://gymlog.ru/programs/'

filters = {
    "category_muscle_mass": (By.XPATH, '//input[@name="category" and @value="1"]//ancestor::div[1]'),
    "category_strength": (By.XPATH, '//input[@name="category" and @value="2"]//ancestor::div[1]'),
    "category_fat_burning": (By.XPATH, '//input[@name="category" and @value="3"]//ancestor::div[1]'),
    "category_star_programs": (By.XPATH, '//input[@name="category" and @value="8"]//ancestor::div[1]'),
    "type_split": (By.XPATH, '//input[@name="type" and @value="1"]//ancestor::div[1]'),
    "type_full_body": (By.XPATH, '//input[@name="type" and @value="3"]//ancestor::div[1]'),
    "type_muscle_groups": (By.XPATH, '//input[@name="type" and @value="2"]//ancestor::div[1]'),
    "period_one_day": (By.XPATH, '//input[@name="period" and @value="1"]//ancestor::div[1]'),
    "period_two_days": (By.XPATH, '//input[@name="period" and @value="2"]//ancestor::div[1]'),
    "period_three_days": (By.XPATH, '//input[@name="period" and @value="3"]//ancestor::div[1]'),
    "period_four_days": (By.XPATH, '//input[@name="period" and @value="4"]//ancestor::div[1]'),
    "period_five_days": (By.XPATH, '//input[@name="period" and @value="5"]//ancestor::div[1]'),
    "period_six_days": (By.XPATH, '//input[@name="period" and @value="6"]//ancestor::div[1]'),
    "level_junior" : (By.XPATH, '//input[@name="level" and @value="1"]//ancestor::div[1]'),
    "level_middle": (By.XPATH, '//input[@name="level" and @value="2"]//ancestor::div[1]'),
    "level_pro": (By.XPATH, '//input[@name="level" and @value="3"]//ancestor::div[1]'),
    "sex_male": (By.XPATH, '//input[@name="sex" and @value="1"]//ancestor::div[1]'),
    "sex_female": (By.XPATH, '//input[@name="sex" and @value="2"]//ancestor::div[1]'),
    "sex_male_and_female": (By.XPATH, '//input[@name="sex" and @value="3"]//ancestor::div[1]')
}
display_programs = (By.XPATH, '//div[@style = "display: block;"]/a')


class ProgramsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(LINK_PROGRAMS)

    def return_attribute(self, element, attribute):
        return self.find(*filters[element]).get_attribute(attribute)

    def click_filter_attribute(self, name):
        self.find(*filters[name]).click()
        k, v = filters[name]
        return self.find(k, v + '//ancestor::label[1]').text

    def select_all_filters(self):
        for k in filters:
            self.click_filter_attribute(k)

    def list_programs_filtering(self):
        return self.find_all(*display_programs)

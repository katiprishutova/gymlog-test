from pages.login_page import LoginPage
from pages.my_programs_page import MyProgramsPage
from pages.create_new_program_page import CreateNewProgramPage
from time import sleep

login = "User390"
password = "bDbiJc"


def test_open_my_programs(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(driver, login, password)
    my_programs_page = MyProgramsPage(driver)
    my_programs_page.open_my_programs_from_start()
    assert driver.title.find("Программы тренировок пользователя") >= 0


def test_create_new_private_program(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(driver, login, password)
    my_programs_page = MyProgramsPage(driver)
    my_programs_page.open_my_programs_from_start()
    my_programs_page.click_new_program()
    create_new_program_page = CreateNewProgramPage(driver)
    create_new_program_page.fill_name_field("Программа приватная 1")
    create_new_program_page.click_save_button()
    my_programs_page.open_my_programs_from_start()
    sleep(5)
    assert my_programs_page.is_private("Программа приватная 1")


def test_create_new_public_program(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(driver, login, password)
    my_programs_page = MyProgramsPage(driver)
    my_programs_page.open_my_programs_from_start()
    my_programs_page.click_new_program()
    create_new_program_page = CreateNewProgramPage(driver)
    create_new_program_page.fill_name_field("Программа публичная 1")
    create_new_program_page.mark_checkbox_public()
    create_new_program_page.click_save_button()
    my_programs_page.open_my_programs_from_start()
    assert not my_programs_page.is_private("Программа публичная 1")


def test_delete_program(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(driver, login, password)
    my_programs_page = MyProgramsPage(driver)
    my_programs_page.open_my_programs_from_start()
    name = my_programs_page.delete_program(driver)
    assert not my_programs_page.is_program_exists(name)


def test_check_category(driver):
    login_page = LoginPage(driver)
    login_page.open()
    name = "Программа для проверки категории"
    login_page.login(driver, login, password)
    my_programs_page = MyProgramsPage(driver)
    my_programs_page.open_my_programs_from_start()
    my_programs_page.click_new_program()
    create_new_program_page = CreateNewProgramPage(driver)
    create_new_program_page.fill_name_field(name)
    list_categories = [create_new_program_page.fill_categories(), create_new_program_page.fill_categories()]
    create_new_program_page.click_save_button()
    my_programs_page.open_my_programs_from_start()
    list_total_categories = my_programs_page.return_program_categories(name)
    assert list_categories.sort() == list_total_categories.sort()

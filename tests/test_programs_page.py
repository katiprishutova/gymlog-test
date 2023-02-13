from pages.programs_page import ProgramsPage
from pages.program_page import ProgramPage
import random
from time import sleep


def test_select_category_muscle_mass(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("category_muscle_mass", "class")
    programs_page.click_filter_attribute("category_muscle_mass")
    status_after = programs_page.return_attribute("category_muscle_mass", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_category_strength(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("category_strength", "class")
    programs_page.click_filter_attribute("category_strength")
    status_after = programs_page.return_attribute("category_strength", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_category_fat_burning(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("category_fat_burning", "class")
    programs_page.click_filter_attribute("category_fat_burning")
    status_after = programs_page.return_attribute("category_fat_burning", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_category_star_programs(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("category_star_programs", "class")
    programs_page.click_filter_attribute("category_star_programs")
    status_after = programs_page.return_attribute("category_star_programs", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_type_split(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("type_split", "class")
    programs_page.click_filter_attribute("type_split")
    status_after = programs_page.return_attribute("type_split", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_type_full_body(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("type_full_body", "class")
    programs_page.click_filter_attribute("type_full_body")
    status_after = programs_page.return_attribute("type_full_body", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_type_muscle_groups(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("type_muscle_groups", "class")
    programs_page.click_filter_attribute("type_muscle_groups")
    status_after = programs_page.return_attribute("type_muscle_groups", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_period_one_day(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("period_one_day", "class")
    programs_page.click_filter_attribute("period_one_day")
    status_after = programs_page.return_attribute("period_one_day", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_period_two_days(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("period_two_days", "class")
    programs_page.click_filter_attribute("period_two_days")
    status_after = programs_page.return_attribute("period_two_days", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_period_three_days(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("period_three_days", "class")
    programs_page.click_filter_attribute("period_three_days")
    status_after = programs_page.return_attribute("period_three_days", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_period_four_days(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("period_four_days", "class")
    programs_page.click_filter_attribute("period_four_days")
    status_after = programs_page.return_attribute("period_four_days", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_period_five_days(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("period_five_days", "class")
    programs_page.click_filter_attribute("period_five_days")
    status_after = programs_page.return_attribute("period_five_days", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_period_six_days(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("period_six_days", "class")
    programs_page.click_filter_attribute("period_six_days")
    status_after = programs_page.return_attribute("period_six_days", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_level_junior(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("level_junior", "class")
    programs_page.click_filter_attribute("level_junior")
    status_after = programs_page.return_attribute("level_junior", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_level_middle(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("level_middle", "class")
    programs_page.click_filter_attribute("level_middle")
    status_after = programs_page.return_attribute("level_middle", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_level_pro(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("level_pro", "class")
    programs_page.click_filter_attribute("level_pro")
    status_after = programs_page.return_attribute("level_pro", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_sex_male(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("sex_male", "class")
    programs_page.click_filter_attribute("sex_male")
    status_after = programs_page.return_attribute("sex_male", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_sex_female(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("sex_female", "class")
    programs_page.click_filter_attribute("sex_female")
    status_after = programs_page.return_attribute("sex_female", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_select_sex_male_and_female(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    status_before = programs_page.return_attribute("sex_male_and_female", "class")
    programs_page.click_filter_attribute("sex_male_and_female")
    status_after = programs_page.return_attribute("sex_male_and_female", "class")
    assert status_before != status_after \
           and (status_before.find("checked") >= 0) ^ bool(status_after.find("checked") >= 0 == 1), "Статус не изменен"


def test_check_correct_filtering(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    begin_link = driver.current_url
    programs_page.select_all_filters()
    list_sexes = [programs_page.click_filter_attribute("sex_male")]
    list_levels = [programs_page.click_filter_attribute("level_middle")]
    list_periods = [programs_page.click_filter_attribute("period_three_days")]
    list_types = [programs_page.click_filter_attribute("type_muscle_groups")]
    list_categories = [programs_page.click_filter_attribute("category_muscle_mass")]
    display_programs = programs_page.list_programs_filtering()
    for test_program in display_programs:
        element_href = test_program.get_attribute("href")
        test_program.click()
        driver = programs_page.move_between_windows(driver, element_href)
        program_page = ProgramPage(driver)
        list_params = program_page.return_list_params()
        list_categories_total = [list_params[0].find(i) >= 0 for i in list_categories]
        list_types_total = [list_params[1].find(i) >= 0 for i in list_types]
        list_levels_total = [list_params[2].find(i) >= 0 for i in list_levels]
        list_sexes_total = [list_params[3].find(i) >= 0 for i in list_sexes]
        list_periods_total = [list_params[4].find(i) >= 0 for i in list_periods]
        assert any(list_sexes_total) * any(list_levels_total) * any(list_periods_total) * \
               any(list_types_total) * any(list_categories_total), "Параметры программы не соответствуют фильтрам"
        driver = programs_page.move_between_windows(driver, begin_link)


def test_check_correct_polyfiltering(driver):
    programs_page = ProgramsPage(driver)
    programs_page.open()
    begin_link = driver.current_url
    programs_page.select_all_filters()
    list_sexes = [programs_page.click_filter_attribute("sex_male"), programs_page.click_filter_attribute("sex_female")]
    list_levels = [programs_page.click_filter_attribute("level_middle"),
                   programs_page.click_filter_attribute("level_pro")]
    list_periods = [programs_page.click_filter_attribute("period_three_days"),
                    programs_page.click_filter_attribute("period_two_days")]
    list_types = [programs_page.click_filter_attribute("type_muscle_groups"),
                  programs_page.click_filter_attribute("type_full_body"),
                  programs_page.click_filter_attribute("type_split")]
    list_categories = [programs_page.click_filter_attribute("category_muscle_mass"),
                       programs_page.click_filter_attribute("category_star_programs"),
                       programs_page.click_filter_attribute("category_strength")]
    display_programs = programs_page.list_programs_filtering()
    for test_program in display_programs:
        element_href = test_program.get_attribute("href")
        test_program.click()
        driver = programs_page.move_between_windows(driver, element_href)
        program_page = ProgramPage(driver)
        list_params = program_page.return_list_params()
        list_categories_total = [list_params[0].find(i) >= 0 for i in list_categories]
        list_types_total = [list_params[1].find(i) >= 0 for i in list_types]
        list_levels_total = [list_params[2].find(i) >= 0 for i in list_levels]
        list_sexes_total = [list_params[3].find(i) >= 0 for i in list_sexes]
        list_periods_total = [list_params[4].find(i) >= 0 for i in list_periods]
        assert any(list_sexes_total) * any(list_levels_total) * any(list_periods_total) * \
               any(list_types_total) * any(list_categories_total), "Параметры программы не соответствуют фильтрам"
        driver = programs_page.move_between_windows(driver, begin_link)

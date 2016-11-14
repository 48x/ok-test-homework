from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tools import locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class OKBrowser:
    MAIN_PAGE_URL = "https://ok.ru"
    SETTINGS_PAGE_URL = "https://ok.ru/settings"

    SETTINGS_FIELDS = {
        "first_name": ".//*[@id='field_name']",
        "last_name": ".//*[@id='field_surname']",
        "day_birthday": ".//*[@id='field_bday']",
        "month_birthday": ".//*[@id='field_bmonth']",
        "year_birthday": ".//*[@id='field_byear']",
        "current_city_search": ".//*[@id='field_citySugg_SearchInput']",
        "origin_city_search": ".//*[@id='field_cityBSugg_SearchInput']",
    }

    def __init__(self):
        self.browser = webdriver.Chrome('../resources/chromedriver')
        self.browser.set_window_size(1024, 768)
        self.browser.set_page_load_timeout(10)

    def open_main_page(self):
        return self.browser.get(self.MAIN_PAGE_URL)

    def log_in(self, login, password):
        name_input = self.browser.find_element_by_xpath(locators.Credentials.LOGIN)
        pass_input = self.browser.find_element_by_xpath(locators.Credentials.PASSWORD)
        submit_button = self.browser.find_element_by_xpath(locators.Credentials.SUBMIT_BUTTON)
        name_input.send_keys(login)
        pass_input.send_keys(password)
        submit_button.click()

    def open_settings_page(self):
        self.browser.get(self.SETTINGS_PAGE_URL)

    def set_locale(self, language):
        self.browser.find_element_by_xpath(locators.Language.MENU).click()
        self.browser.find_element_by_xpath(language).click()

    def open_edit_setting_dialog(self):
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath(locators.SettingsPage.SETTINGS_DIALOG).click()

    def user_settings_action(self, action):
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath(locators.SettingsDialog.BUTTONS.get(action)).click()

    def set_text_setting(self, text_field, value):
        self.browser.implicitly_wait(5)
        setting_web_element = self.browser.find_element_by_xpath(locators.SettingsDialog.TEXT_FIELDS.get(text_field))
        setting_web_element.clear()
        setting_web_element.send_keys(value)

    def get_select_setting_options_list(self, select_field):
        self.browser.implicitly_wait(5)
        select_web_element = Select(self.browser.find_element_by_xpath(
            locators.SettingsDialog.SELECT_FIELDS.get(select_field))
        )
        return [option.text for option in select_web_element.options]

    def set_select_setting(self, select_field, value):
        self.browser.implicitly_wait(5)
        select_web_element = Select(self.browser.find_element_by_xpath(
            locators.SettingsDialog.SELECT_FIELDS.get(select_field))
        )
        if value is None:
            select_web_element.select_by_index(0)
        elif isinstance(value, int):
            select_web_element.select_by_index(value)
        else:
            select_web_element.select_by_value(value)

    def set_gender(self, gender):
        self.browser.implicitly_wait(5)
        if gender == "male":
            gender_button_web_element = self.browser.find_element_by_xpath(".//*[@id='field_gender_1']")
        else:
            gender_button_web_element = self.browser.find_element_by_xpath(".//*[@id='field_gender_2']")
        gender_button_web_element.click()

    def get_gender(self):
        male_button_web_element = self.browser.find_element_by_xpath(".//*[@id='field_gender_1']")
        female_button_web_element = self.browser.find_element_by_xpath(".//*[@id='field_gender_2']")
        if male_button_web_element.is_selected():
            return "male"
        if female_button_web_element.is_selected():
            return "female"

    def get_error_text_for_setting(self, field_with_error, error_text):
        try:
            WebDriverWait(self.browser, 10).until(
                expected_conditions.text_to_be_present_in_element(
                    (
                        By.XPATH,
                        locators.SettingsDialog.ERROR_FIELDS.get(field_with_error)),
                    error_text)
            )
            error_text_web_element = self.browser.find_element_by_xpath(locators.SettingsDialog.ERROR_FIELDS.get(field_with_error))
        except NoSuchElementException:
            return "No element found"
        return error_text_web_element.text

    def get_text_setting_value(self, text_field):
        self.browser.implicitly_wait(5)
        setting_web_element = self.browser.find_element_by_xpath(locators.SettingsDialog.TEXT_FIELDS.get(text_field))
        return setting_web_element.get_attribute("value")

    def get_select_setting_value(self, select_field):
        self.browser.implicitly_wait(5)
        select_web_element = Select(self.browser.find_element_by_xpath(
            locators.SettingsDialog.SELECT_FIELDS.get(select_field))
        )
        return select_web_element.first_selected_option.text

    def close(self):
        self.browser.close()
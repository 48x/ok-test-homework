import unittest
import os
from configparser import RawConfigParser
from tools.browser import OKBrowser
from tools.locators import Language
import time


class BasicTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = RawConfigParser()
        config.read("{}/../config.conf".format(os.path.dirname(__file__)))
        user_login = config.get("Credentials", "ok.login")
        user_password = config.get("Credentials", "ok.password")
        cls.ok_browser = OKBrowser()
        cls.ok_browser.open_main_page()
        cls.ok_browser.set_locale(Language.RU)
        cls.ok_browser.log_in(user_login, user_password)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.ok_browser.close()

    def setUp(self):
        self.ok_browser.open_edit_setting_dialog()

    def tearDown(self):
        self.ok_browser.user_settings_action('cancel')
        time.sleep(3)


class TestInvalidDataHandling(BasicTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestInvalidDataHandling, cls).setUpClass()
        cls.ok_browser.open_settings_page()

    def test_first_name_is_empty(self):
        self.ok_browser.set_text_setting("first_name", "")
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("first_name", "Пожалуйста, укажите ваше имя."),
            "Пожалуйста, укажите ваше имя."
        )

    def test_last_name_is_empty(self):
        self.ok_browser.set_text_setting("last_name", "s")
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("last_name", "Пожалуйста, укажите вашу фамилию."),
            "Пожалуйста, укажите вашу фамилию."
        )

    def test_birthday_day_is_not_selected(self):
        self.ok_browser.set_select_setting("day_birthday", None)
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("birthday", "День вашего рождения указан некорректно."),
            "День вашего рождения указан некорректно."
        )

    def test_birthday_month_is_not_selected(self):
        self.ok_browser.set_select_setting("month_birthday", None)
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("birthday", "День вашего рождения указан некорректно."),
            "День вашего рождения указан некорректно."
        )

    def test_birthday_year_is_not_selected(self):
        self.ok_browser.set_select_setting("year_birthday", None)
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("birthday", "День вашего рождения указан некорректно."),
            "День вашего рождения указан некорректно."
        )

    def test_current_city_is_not_selected(self):
        self.ok_browser.set_text_setting("current_city", "")
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("current_city", "Пожалуйста, выберите место проживания из списка"),
            "Пожалуйста, выберите место проживания из списка"
        )

    def test_current_city_is_not_in_list(self):
        self.ok_browser.set_text_setting("current_city", "lalala")
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("current_city", "Пожалуйста, выберите место проживания из списка"),
            "Пожалуйста, выберите место проживания из списка"
        )

    def test_origin_city_is_not_in_list(self):
        self.ok_browser.set_text_setting("origin_city", "lalala")
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("origin_city", "Пожалуйста, выберите родной город из списка."),
            "Пожалуйста, выберите родной город из списка."
        )

    def test_day_birthday_is_invalid_for_month(self):
        self.ok_browser.set_select_setting("day_birthday", "31")
        self.ok_browser.set_select_setting("month_birthday", 2)
        self.ok_browser.set_select_setting("year_birthday", "1990")
        self.ok_browser.user_settings_action("submit")
        self.assertEqual(
            self.ok_browser.get_error_text_for_setting("birthday", "День вашего рождения указан некорректно."),
            "День вашего рождения указан некорректно."
        )


class TestInputFieldsLength(BasicTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestInputFieldsLength, cls).setUpClass()
        cls.ok_browser.open_settings_page()


class TestUserInfoUpdateChecks(BasicTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestUserInfoUpdateChecks, cls).setUpClass()
        cls.ok_browser.open_settings_page()

    def test_first_name_is_updated(self):
        self.ok_browser.set_text_setting("first_name", "Valeriy")
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_text_setting_value("first_name"), "Valeriy")

    def test_last_name_is_updated(self):
        self.ok_browser.set_text_setting("last_name", "Valeriev")
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_text_setting_value("last_name"), "Valeriev")

    def test_day_birthday_is_updated(self):
        self.ok_browser.set_select_setting("day_birthday", "22")
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_select_setting_value("day_birthday"), "22")

    def test_month_birthday_is_updated(self):
        self.ok_browser.set_select_setting("month_birthday", 3)
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_select_setting_value("month_birthday"), "март")

    def test_year_birthday_is_updated(self):
        self.ok_browser.set_select_setting("year_birthday", "1976")
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_select_setting_value("year_birthday"), "1976")

    def test_gender_is_updated(self):
        self.ok_browser.set_gender("male")
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_gender(), "male")

    def test_current_city_is_updated(self):
        self.ok_browser.set_text_setting("current_city", "Астрахань, Россия")
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_text_setting_value("current_city"), "Астрахань, Россия")

    def test_origin_city_is_updated(self):
        self.ok_browser.set_text_setting("origin_city", "Астрахань, Россия")
        self.ok_browser.user_settings_action("submit")
        time.sleep(3)
        self.ok_browser.user_settings_action("accept_changes")
        self.ok_browser.open_edit_setting_dialog()
        time.sleep(3)
        self.assertEqual(self.ok_browser.get_text_setting_value("origin_city"), "Астрахань, Россия")

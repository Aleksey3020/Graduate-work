import time

from selenium import webdriver
from page_object.base_page import BasePage
from locators.registration import ExitRegistrationLocators


class ExitAndRegistration(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/'

# Проверка наличия ошибки 'Поля обязательное для заполнения'
    def check_for_error(self):
        self.click_element(ExitRegistrationLocators.login_and_register_button)
        self.click_element(ExitRegistrationLocators.register_button1)
        self.click_element(ExitRegistrationLocators.register_button2)
        error_text = self.find_element(ExitRegistrationLocators.locator_error1_text).text
        assert error_text == 'Поле обязательно для заполнения'

# Проверка наличии ошибки 'Некорректный e-mail'
    def email_validation(self):
        self.send_keys(ExitRegistrationLocators.locator_email, 'illya.krug@yandex,ru')
        self.click_element(ExitRegistrationLocators.register_button2)
        error_email = self.find_element(ExitRegistrationLocators.locator_error_email)
        assert error_email.is_displayed()
        assert error_email.text == 'Некорректный e-mail'

# Проверка, на не совпадение кодов страны
    def checking_country_codes(self):
        self.click_element(ExitRegistrationLocators.country_selection_button)
        belarus = self.find_element(ExitRegistrationLocators. country_code_belarus).text
        kazakhstan = self.find_element(ExitRegistrationLocators. country_code_kazakhstan).text
        assert belarus != kazakhstan

# Проверка, на совпадение кодов страны
    def checking2_country_codes(self):
        kazakhstan = self.find_element(ExitRegistrationLocators. country_code_kazakhstan).text
        russia = self.find_element(ExitRegistrationLocators.russia_country_code).text
        assert russia == kazakhstan
        self.click_element(ExitRegistrationLocators.country_selection_button)

# Проверка наличии ошибки 'Минимум 6 символов'
    def symbol_count_check(self):
        self.send_keys(ExitRegistrationLocators.password_5_symbol, '12124')
        self.click_element(ExitRegistrationLocators.register_button2)
        error_password = self.find_element(ExitRegistrationLocators.locator_error_password)
        assert error_password.is_displayed()
        assert error_password.text == 'Минимум 6 символов'

# Проверка наличие кнопки видимость пороля и ее кликабельность
    def password_visibility_button(self):
        assert self.find_element(ExitRegistrationLocators.locator_password1_visibility).is_displayed()
        assert self.find_element(ExitRegistrationLocators.locator_password2_visibility).is_displayed()
        self.click_element(ExitRegistrationLocators.locator_password1_visibility)
        self.click_element(ExitRegistrationLocators.locator_password2_visibility)

# Проверка кликабельности кнопки 'Авторизация'
    def verification_button_authorization(self):
        assert self.find_element(ExitRegistrationLocators.authorization_button).is_displayed()
        self.click_element(ExitRegistrationLocators.authorization_button)
        time.sleep(4)
        assert self.find_element(ExitRegistrationLocators.authorization_tab_element).is_displayed()
        self.click_element(ExitRegistrationLocators.exit_authorization)



import time
from selenium import webdriver
from page_object.base_page import BasePage
from locators.sign_in_registration_locators import SignInRegistrationLocators
import allure


class SignInAndRegistration(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/'

    @allure.step('Open sign in and registration')
    def open_registration(self):
        self.click_element(SignInRegistrationLocators.login_and_register_button)
        self.click_element(SignInRegistrationLocators.register_button1)
        time.sleep(3)

    @allure.step('Checking the error text')
    def check_for_error(self):
        self.click_element(SignInRegistrationLocators.register_button2)
        assert self.get_text(SignInRegistrationLocators.locator_error1_text) == 'Поле обязательно для заполнения'
        allure.attach('Поле обязательно для заполнения', name='Error text')

    @allure.step('Checking visibility and text email errors')
    def email_validation(self):
        self.send_keys(SignInRegistrationLocators.locator_email, 'pischuksyandex,ru')
        self.click_element(SignInRegistrationLocators.register_button2)
        assert self.find_visible_element(SignInRegistrationLocators.locator_error_email).is_displayed()
        assert self.get_text(SignInRegistrationLocators.locator_error_email) == 'Некорректный e-mail'
        allure.attach('Некорректный e-mail', name='Error email text')

    @allure.step('Check for mismatch of country codes Belarus and Kazakhstan')
    def checking_country_codes(self):
        self.click_element(SignInRegistrationLocators.country_selection_button)
        belarus = self.get_text(SignInRegistrationLocators. country_code_belarus)
        kazakhstan = self.get_text(SignInRegistrationLocators. country_code_kazakhstan)
        assert belarus != kazakhstan

    @allure.step('Checking for coincidence of country codes Russia and Kazakhstan')
    def checking2_country_codes(self):
        self.click_element(SignInRegistrationLocators.country_selection_button)
        kazakhstan = self.get_text(SignInRegistrationLocators.country_code_kazakhstan)
        russia = self.get_text(SignInRegistrationLocators.russia_country_code)
        assert russia == kazakhstan
        self.click_element(SignInRegistrationLocators.country_selection_button)

    @allure.step('Checking the visibility and text of a password error')
    def password_validation(self):
        self.send_keys(SignInRegistrationLocators.password_5_symbol, '12124')
        self.click_element(SignInRegistrationLocators.register_button2)
        assert self.find_visible_element(SignInRegistrationLocators.locator_error_password).is_displayed()
        assert self.get_text(SignInRegistrationLocators.locator_error_password) == 'Минимум 6 символов'
        allure.attach('Минимум 6 символов', name='Error password text')

    @allure.step('Checking visibility button')
    def password_visibility_button(self):
        assert self.find_visible_element(SignInRegistrationLocators.locator_password1_visibility).is_displayed()
        assert self.find_visible_element(SignInRegistrationLocators.locator_password2_visibility).is_displayed()
        self.click_element(SignInRegistrationLocators.locator_password1_visibility)
        self.click_element(SignInRegistrationLocators.locator_password2_visibility)

    @allure.step('checking the visibility of the  authorization button')
    def button_authorization(self):
        assert self.find_visible_element(SignInRegistrationLocators.authorization_button).is_displayed()
        self.click_element(SignInRegistrationLocators.authorization_button)
        time.sleep(3)
        assert self.find_visible_element(SignInRegistrationLocators.authorization_tab_element).is_displayed()
        self.click_element(SignInRegistrationLocators.exit_authorization)

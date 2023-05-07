import time
from selenium import webdriver
from page_object.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
import allure


class PersonalAccount (BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/'

    @allure.step('Login to your personal account')
    def login_account(self):
        self.click_element(PersonalAccountLocators.login_and_register_button)
        self.send_keys(PersonalAccountLocators.email_input, 'vgugnevich@yandex.ru')
        self.send_keys(PersonalAccountLocators.password_input, 'qwer2121rewQ')
        self.click_element(PersonalAccountLocators.login_button)
        time.sleep(5)
        self.click_element(PersonalAccountLocators.cart_button)
        time.sleep(3)
        self.click_element(PersonalAccountLocators.go_to_checkout_button)
        time.sleep(3)

    @allure.step('Checking the entrance to your personal account by text')
    def checking_personal_account(self):
        assert self.get_text(PersonalAccountLocators.open_personal_account) == 'Гугневич Вадим'
        allure.attach('Гугневич Вадим', name='Text in personal account')

    @allure.step('Checking price change from quantity')
    def price_change_check(self):
        self.click_element(PersonalAccountLocators.plus_button)
        time.sleep(3)
        price_value = self.get_text(PersonalAccountLocators.locator_price_value)
        total_payable = self.get_text(PersonalAccountLocators.locator_total_payable)
        assert price_value == total_payable

    @allure.step('Checking visibility and order status text')
    def checking_order_status(self):
        self.click_element(PersonalAccountLocators.payment_method)
        time.sleep(2)
        self.click_element(PersonalAccountLocators.checkout_button)
        time.sleep(2)
        assert self.find_visible_element(PersonalAccountLocators.locator_your_order).is_displayed()
        assert self.get_text(PersonalAccountLocators.locator_your_order) == 'Спасибо за Ваш заказ.'
        allure.attach('Спасибо за Ваш заказ.', name='Open window text')

    @allure.step('Status string text check')
    def check_string_status(self):
        assert self.get_text(PersonalAccountLocators.locator_string_status) == 'Принят'
        allure.attach('Принят', name='Status text')

    @allure.step('Checking button text go to payment')
    def checking_the_proceed_to_payment_button(self):
        assert self.get_text(PersonalAccountLocators.locator_go_to_payment) == 'Перейти к оплате'
        allure.attach('Перейти к оплате', name='Button text')
        self.click_element(PersonalAccountLocators.locator_go_to_payment)

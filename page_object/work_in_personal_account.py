from selenium import webdriver
from page_object.base_page import BasePage
from locators.personal_account import PersonalAccountLocators


class PersonalAccount (BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/'

# Проверка на то, что мы вошли в личный кабинет
    def checking_personal_account(self):
        self.click_element(PersonalAccountLocators.login_and_register_button)
        self.send_keys(PersonalAccountLocators.email_input, 'illya.krug@yandex.ru')
        self.send_keys(PersonalAccountLocators.password_input, 'qwer21rewq34')
        self.click_element(PersonalAccountLocators.login_button)
        assert self.find_element(PersonalAccountLocators.open_personal_account).text == 'Круг Илья'

# Проверяем изменение цены относительно выбора количество изделий
    def price_change_check(self):
        self.click_element(PersonalAccountLocators.cart_button)
        self.click_element(PersonalAccountLocators.go_to_checkout_button)
        self.click_element(PersonalAccountLocators.plus_button)
        price_value = self.find_element(PersonalAccountLocators.locator_price_value).text
        total_payable = self.find_element(PersonalAccountLocators.locator_total_payable).text
        assert price_value == total_payable

# Проверяем кнопки оформить заказ
    def checking_order_status(self):
        #self.send_keys(PersonalAccountLocators.string_street, 'Ленина')
        self.find_element(PersonalAccountLocators.string_street).clear()
        #self.send_keys(PersonalAccountLocators.string_house, '79')
        #self.send_keys(PersonalAccountLocators.string_flat, '2')
        self.click_element(PersonalAccountLocators.payment_method)
        self.click_element(PersonalAccountLocators.checkout_button)
        your_order = self.find_element(PersonalAccountLocators.locator_your_order).text
        assert self.find_element(PersonalAccountLocators.locator_your_order).is_displayed()
        assert your_order == 'Спасибо за Ваш заказ.'

# Проверка строки статус.
    def check_string_status(self):
        string_status = self.find_element(PersonalAccountLocators.locator_string_status).text
        assert string_status == 'Принят'

# Проверка кнопки перейти к оплате
    def checking_the_proceed_to_payment_button(self):
        assert self.find_element(PersonalAccountLocators.locator_go_to_payment).text == 'Перейти к оплате'
        self.click_element(PersonalAccountLocators.locator_go_to_payment)








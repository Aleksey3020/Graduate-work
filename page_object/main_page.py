import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from page_object.base_page import BasePage
from locators.main import MainPageLocators


class ShopMainPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/'

# Проверяем является ли данная страница ожидаемой
    def checking_main_page_for_expectation(self):
        assert self.url == self.webdriver.current_url

# Наличие и кликабельность кнопки связаться с консультантом и наличие надписи обратная связь
    def feedback_button_test(self):
        self.click_element(MainPageLocators.feedback)
        time.sleep(3)
        assert self.find_element(MainPageLocators.text_feedback).text == 'Обратная связь'

# Проверяем наличие ошибки при некорректном вводе email в обратной связи, выход
    def email_error_checking(self):
        self.send_keys(MainPageLocators.email_in_feedback, 'illya.krugyandex.ru')
        self.click_element(MainPageLocators.send_button)
        error2 = self.find_element(MainPageLocators.email_error)
        assert error2.text == 'Указан неверный Емейл'
        assert error2.is_displayed()
        self.click_element(MainPageLocators.exit_feedback)

# Проверяем наличие элемента GALANTEYA на главной страницы
    def check_element1_for_pending(self):
        assert self.find_element(MainPageLocators.visible_element1_main_page).is_displayed()

# Проверяем наличие кнопки Вход/Pегистрация на главной страницы
    def check_element2_for_pending(self):
        assert self.find_element(MainPageLocators.visible_element2_main_page).is_displayed()

# Проверка на ожидаемость города от выбранной страны Россия
    def expected_city_of_moscow(self):
        self.click_element(MainPageLocators.country_russia)
        assert self.find_element(MainPageLocators.locator_city).text == 'Москва'

# Проверка на ожидаемость города от выбранной страны Буларусь
    def expected_city_of_minsk(self):
        self.click_element(MainPageLocators.country_belarus)
        assert self.find_element(MainPageLocators.locator_city).text == 'Минск'

# Проверяем наличие ошибки при некорректном вводе email
    def error_incorrect_email_input(self):
        self.send_keys(MainPageLocators.email_input_line, 'illya.krugyandex.ru')
        self.click_element(MainPageLocators.subscribe_button)
        error1 = self.find_element(MainPageLocators.email_text_error)
        assert error1.text == 'Некорректный e-mail'
        assert error1.is_displayed()

# Переходим в вкладку каталог интернет магазина
    def catalog_muzhchinam(self):
        self.click_element(MainPageLocators.catalog)

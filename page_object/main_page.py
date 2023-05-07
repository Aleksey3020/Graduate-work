import time
from selenium import webdriver
from page_object.base_page import BasePage
from locators.main_locators import MainPageLocators
import allure


class ShopMainPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/'

    @allure.step('Page expectancy check')
    def checking_main_page_for_expectation(self):
        assert self.url == self.webdriver.current_url

    @allure.step('Checking the visibility of an element "GALANTEYA"')
    def check_element1_for_pending(self):
        assert self.find_visible_element(MainPageLocators.visible_element1_main_page).is_displayed()

    @allure.step('Feedback button operation test')
    def feedback_button_test(self):
        self.click_element(MainPageLocators.feedback)
        time.sleep(2)
        assert self.get_text(MainPageLocators.text_feedback) == 'Обратная связь'
        allure.attach('Обратная связь', name='Оpen window text feedback')

    @allure.step('Сhecking for an error and its text if the email is entered incorrectly')
    def email_error_checking(self):
        self.send_keys(MainPageLocators.email_in_feedback, 'pischuksyandex.ru')
        self.click_element(MainPageLocators.send_button)
        assert self.get_text(MainPageLocators.email_error) == 'Указан неверный Емейл'
        allure.attach('Указан неверный Емейл', name='Feedback error text')
        assert self.find_visible_element(MainPageLocators.email_error).is_displayed()
        self.click_element(MainPageLocators.exit_feedback)

    @allure.step('Checking the visibility of an element "Login and registration"')
    def check_element2_for_pending(self):
        assert self.find_visible_element(MainPageLocators.visible_element2_main_page).is_displayed()

    @allure.step('Сhecking for the expected text Moscow')
    def expected_city_of_moscow(self):
        self.click_element(MainPageLocators.country_russia)
        assert self.get_text(MainPageLocators.locator_city) == 'Москва'
        allure.attach('Москва', name='Expected city of Russia')

    @allure.step('Сhecking for the expected text Minsk')
    def expected_city_of_minsk(self):
        self.click_element(MainPageLocators.country_belarus)
        assert self.get_text(MainPageLocators.locator_city) == 'Минск'
        allure.attach('Минск', name='expected city of Belarus')

    @allure.step('Сhecking for an error and its text if the email is entered incorrectly')
    def error_incorrect_email_input(self):
        self.send_keys(MainPageLocators.email_input_line, 'pischuks@yand,ru')
        self.click_element(MainPageLocators.subscribe_button)
        assert self.get_text(MainPageLocators.email_text_error) == 'Некорректный e-mail'
        allure.attach('Некорректный e-mail', name='Error text')
        assert self.find_visible_element(MainPageLocators.email_text_error).is_displayed()

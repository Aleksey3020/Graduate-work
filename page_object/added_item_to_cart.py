import time
from selenium import webdriver
from page_object.base_page import BasePage
from locators.cart_locators import CartLocators
import allure


class AddToCart(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/catalog/muzhchinam_1-204/'

    @allure.step('Сhecking the visibility and text of the product in the cart')
    def check_add_to_cart_button(self):
        assert self.get_text(CartLocators.text_button) == 'Добавить в корзину'
        allure.attach('Добавить в корзину', name='Button text')
        self.click_element(CartLocators.add_to_cart_button)
        time.sleep(2)
        assert self.get_text(CartLocators.item_in_cart) == '1 товар'
        allure.attach('1 товар', name='Expected text when added to cart')
        assert self.find_visible_element(CartLocators.item_in_cart).is_displayed()

    @allure.step('Check quantity text in cart parameter')
    def checking_quantity_parameter(self):
        assert self.get_text(CartLocators.amount) == '1 шт.'
        allure.attach('1 шт.', name='Number items in the cart')

    @allure.step('Checking if the price matches the total')
    def price_match_check(self):
        price = self.get_text(CartLocators.locator_price)
        in_total = self.get_text(CartLocators.locator_in_total)
        assert price == in_total

    @allure.step('Checking the visibility and text of the button go to design')
    def check_button_go_to_checkout(self):
        assert self.find_visible_element(CartLocators.go_to_checkout_button).is_displayed()
        assert self.get_text(CartLocators.go_to_checkout_button) == 'Перейти к оформлению'
        allure.attach('Перейти к оформлению', name='Button text')
        self.click_element(CartLocators.cart_exit)

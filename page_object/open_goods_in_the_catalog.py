import time
from selenium import webdriver
from page_object.base_page import BasePage
from locators.open_goods_locators import OpenGoodsLocators
import allure


class OpenGoodsCatalog(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/catalog/muzhchinam_1-204/'

    @allure.step('Opening genuine leather goods')
    def opening_goods(self):
        self.click_element(OpenGoodsLocators.checkbox_genuine_leather)
        time.sleep(2)
        self.click_element(OpenGoodsLocators.product)
        time.sleep(2)

    @allure.step('Checking the text of an open item')
    def product_conformity_check(self):
        assert self.get_text(OpenGoodsLocators.locator_open_product) == 'в наличии'
        allure.attach('в наличии', name='Open item element')

    @allure.step('Checking the text of the expected currency')
    def currency_expectancy_check(self):
        assert self.get_text(OpenGoodsLocators.mani) == 'BYN'
        allure.attach('BYN', name='Expected currency')

    @allure.step('Material visibility check')
    def material(self):
        assert self.find_visible_element(OpenGoodsLocators.material).is_displayed()

    @allure.step('Checking button visibility and quantity visibility')
    def checking_the_favorites_button(self):
        assert self.find_visible_element(OpenGoodsLocators.favorites_button).is_displayed()
        self.click_element(OpenGoodsLocators.favorites_button)
        assert self.find_visible_element(OpenGoodsLocators.quantity_of_selected_item).is_displayed()

    @allure.step('Checking the visibility and text of a product added to favorites')
    def product_expectancy_check(self, ):
        self.click_element(OpenGoodsLocators.open_favorites)
        assert self.get_text(OpenGoodsLocators.product_availability) == '1 товар'
        allure.attach('1 товар', name='Expected text when added to a featured product')
        assert self.find_visible_element(OpenGoodsLocators.product_availability).is_displayed()
        self.click_element(OpenGoodsLocators.locator_exit)

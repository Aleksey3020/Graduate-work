import time

from selenium import webdriver
from page_object.base_page import BasePage
from locators.catalog import CatalogPageLocators


class ShopCatalogPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/catalog/muzhchinam_1-204/'

# Проверка на ожидаемый элемент->мужчинам
    def check_for_expected_element(self):
        assert self.find_element(CatalogPageLocators.element_men).text == 'Мужчинам'

# Проверка на наличие иконки->натуральная кожа
    def presence_of_genuine_leather_icon(self):
        self.click_element(CatalogPageLocators.checkbox_genuine_leather)
        time.sleep(3)
        assert self.find_element(CatalogPageLocators.icon_genuine_leather).is_displayed()
        self.click_element(CatalogPageLocators.checkbox_genuine_leather)
        time.sleep(2)

# Проверка иконки->добавить в избранное
    def presence_of_the_icon_add_to_favorites(self):
        self.click_element(CatalogPageLocators.checkbox_ribbon_belt)
        time.sleep(5)
        assert self.find_element(CatalogPageLocators.icon_add_to_favorites).is_displayed()

# Выбераем синтетическая ткань и кликаем на 1 изделие и провераем открылось ли то изделие которое мы кликнули
    def product_conformity_check(self):
        self.click_element(CatalogPageLocators.checkbox_genuine_leather)
        time.sleep(3)
        self.click_element(CatalogPageLocators.product)
        time.sleep(3)
        assert self.find_element(CatalogPageLocators.locator_open_product_name).text == 'портфель деловой 10413'

# Проверка на ожидаемость валюты
    def currency_expectancy_check(self):
        assert self.find_element(CatalogPageLocators.mani).text == 'BYN'

# Проверка материала
    def material(self):
        assert self.find_element(CatalogPageLocators.material).is_displayed()

# Проверка наличия кнопки избранные товары и ее кликабельность, отображение количество товара над значком
    def checking_the_favorites_button(self):
        assert self.find_element(CatalogPageLocators.favorites_button).is_displayed()
        self.click_element(CatalogPageLocators.favorites_button)
        assert self.find_element(CatalogPageLocators. quantity_of_selected_item).is_displayed()

# Проверка наличие товара в избранные товары и выход назад
    def product_expectancy_check(self, ):
        self.click_element(CatalogPageLocators.open_favorites)
        selected_item = self.find_element(CatalogPageLocators.product_availability)
        assert selected_item.text == '1 товар'
        assert selected_item.is_displayed()
        self.click_element(CatalogPageLocators.locator_exit)

# Проверяем кликабельность и текст Добавить в корзину, наличие добавленного товара в корзине
    def check_add_to_cart_button(self):
        assert self.find_element(CatalogPageLocators.text_button).text == 'Добавить в корзину'
        self.click_element(CatalogPageLocators.add_to_cart_button)
        time.sleep(3)
        item_in_cart = self.find_element(CatalogPageLocators.item_in_cart)
        assert item_in_cart.text == '1 товар'
        assert item_in_cart.is_displayed()

# Проверка параметра 'Количество' в корзине
    def checking_quantity_parameter(self):
        assert self.find_element(CatalogPageLocators.amount).text == '1 шт.'

# Проверка на совпадение параметра цена с ИТОГО
    def price_match_check(self):
        price = self.find_element(CatalogPageLocators.locator_price).text
        in_total = self.find_element(CatalogPageLocators.locator_in_total).text
        assert price == in_total

# Проверка наличие кнопки Перейти к оформлению и ее текст
    def check_button_go_to_checkout(self):
        button_text = self.find_element(CatalogPageLocators.go_to_checkout_button).text
        assert self.find_element(CatalogPageLocators.go_to_checkout_button).is_displayed()
        assert button_text == 'Перейти к оформлению'
        self.click_element(CatalogPageLocators.cart_exit)


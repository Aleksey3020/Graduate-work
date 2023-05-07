import time
from selenium import webdriver
from page_object.base_page import BasePage
from locators.catalog_locators import CatalogPageLocators
import allure


class ShopCatalogPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://galanteya.by/catalog/muzhchinam_1-204/'

    @allure.step("Сhecking expected text 'Мужчинам'")
    def check_for_expected_element(self):
        assert self.get_text(CatalogPageLocators.element_men) == 'Мужчинам'
        allure.attach('Мужчинам', name='Сatalog page element')

    @allure.step('Checking for genuine leather badge')
    def presence_of_genuine_leather_icon(self):
        self.click_element(CatalogPageLocators.checkbox_genuine_leather)
        time.sleep(2)
        assert self.find_visible_element(CatalogPageLocators.icon_genuine_leather).is_displayed()
        self.click_element(CatalogPageLocators.checkbox_genuine_leather)
        time.sleep(2)

    @allure.step('Check for icon add to favorites')
    def presence_of_the_icon_add_to_favorites(self):
        self.click_element(CatalogPageLocators.checkbox_ribbon_belt)
        time.sleep(2)
        assert self.find_visible_element(CatalogPageLocators.icon_add_to_favorites).is_displayed()

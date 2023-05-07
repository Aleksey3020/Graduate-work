from page_object.catalog_page import ShopCatalogPage
import allure


@allure.suite('Checking the catalog site section')
class TestSectionCatalog:
    @allure.title('Check element "Мужчинам" for pending')
    def testing_expected_element(self, browser):
        catalog = ShopCatalogPage(browser)
        catalog.open()
        catalog.check_for_expected_element()

    @allure.title('Test for genuine leather badge')
    def test_for_genuine_leather_badge(self, browser):
        catalog = ShopCatalogPage(browser)
        catalog.open()
        catalog.presence_of_genuine_leather_icon()

    @allure.title('Test presence of the icon add to favorites')
    def test_presence_of_the_icon_add_to_favorites(self, browser):
        catalog = ShopCatalogPage(browser)
        catalog.open()
        catalog.presence_of_the_icon_add_to_favorites()

from page_object.open_goods_in_the_catalog import OpenGoodsCatalog
import allure


@allure.suite('Сhecking open goods')
class TestOpenGoods:
    @allure.title('Сhecking for the opening of the selected product')
    def test_open_the_selected_product(self, browser):
        goods = OpenGoodsCatalog(browser)
        goods.open()
        goods.opening_goods()
        goods.product_conformity_check()

    @allure.title('Product description test')
    def test_product_description(self, browser):
        goods = OpenGoodsCatalog(browser)
        goods.open()
        goods.opening_goods()
        with allure.step('Material test'):
            goods.material()
        with allure.step('Сurrency check test'):
            goods.currency_expectancy_check()

    @allure.title('Testing the favorites button')
    def testing_the_favorites_button(self, browser):
        goods = OpenGoodsCatalog(browser)
        goods.open()
        goods.opening_goods()
        with allure.step('Checking the favorites button'):
            goods.checking_the_favorites_button()
        with allure.step('Checking the availability of goods in favorites'):
            goods.product_expectancy_check()

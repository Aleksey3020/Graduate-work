from page_object.open_goods_in_the_catalog import OpenGoodsCatalog
from page_object.added_item_to_cart import AddToCart
import allure


@allure.suite('Checking the goods added to the cart')
class TestItemInCart:
    @allure.title('Тesting the goods in the cart')
    def testing_the_goods_in_the_cart(self, browser):
        goods = OpenGoodsCatalog(browser)
        goods.open()
        goods.opening_goods()
        cart = AddToCart(browser)
        with allure.step('Check add to cart button'):
            cart.check_add_to_cart_button()
        with allure.step('Checking the quantity parameter in the cart'):
            cart.checking_quantity_parameter()
        with allure.step('Price match check'):
            cart.price_match_check()
        with allure.step('Сheck button go to checkout'):
            cart.check_button_go_to_checkout()

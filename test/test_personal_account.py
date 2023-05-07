from page_object.open_goods_in_the_catalog import OpenGoodsCatalog
from page_object.added_item_to_cart import AddToCart
from page_object.work_in_personal_account import PersonalAccount
import allure


@allure.suite('Check of work in a personal account')
class TestPersonalAccount:
    @allure.title('Checking login to the personal account')
    def test_login_to_the_personal_account(self, browser):
        goods = OpenGoodsCatalog(browser)
        goods.open()
        goods.opening_goods()
        cart = AddToCart(browser)
        cart.check_add_to_cart_button()
        cart.check_button_go_to_checkout()
        account = PersonalAccount(browser)
        account.login_account()
        account.checking_personal_account()

    @allure.title('Price change check')
    def test_price_change(self, browser):
        goods = OpenGoodsCatalog(browser)
        goods.open()
        goods.opening_goods()
        cart = AddToCart(browser)
        cart.check_add_to_cart_button()
        cart.check_button_go_to_checkout()
        account = PersonalAccount(browser)
        account.login_account()
        account.price_change_check()

    @allure.title('Testing checkout button')
    def testing_checkout_button(self, browser):
        goods = OpenGoodsCatalog(browser)
        goods.open()
        goods.opening_goods()
        cart = AddToCart(browser)
        cart.check_add_to_cart_button()
        cart.check_button_go_to_checkout()
        account = PersonalAccount(browser)
        account.login_account()
        with allure.step('Checking order status'):
            account.checking_order_status()
        with allure.step('Checking string status'):
            account.check_string_status()
        with allure.step('Сhecking the proceed to paymen button'):
            account.checking_the_proceed_to_payment_button()

from page_object.main_page import ShopMainPage
import allure


@allure.suite('Checking the main page of the site')
class TestMainPageSite:
    @allure.title('Test waiting for the main page')
    def test_waiting_for_the_main_page(self, browser):
        main = ShopMainPage(browser)
        main.open()
        main.checking_main_page_for_expectation()

    @allure.title('Check element "GALANTEYA" for pending')
    def test_for_the_presence_of_an_element1(self, browser):
        main = ShopMainPage(browser)
        main.open()
        main.check_element1_for_pending()

    @allure.title('Testing feedback and correctness of email input')
    def testing_feedback_and_correctness_of_email_input(self, browser):
        main = ShopMainPage(browser)
        main.open()
        with allure.step('Testing feedback'):
            main.feedback_button_test()
        with allure.step('Testing correctness of email input'):
            main.email_error_checking()

    @allure.title('Check the element "Login and registration" for pending')
    def test_for_the_presence_of_an_element2(self, browser):
        main = ShopMainPage(browser)
        main.open()
        main.check_element2_for_pending()

    @allure.title('Test expected city moscow')
    def test_expected_city_moscow(self, browser):
        main = ShopMainPage(browser)
        main.open()
        main.expected_city_of_moscow()

    @allure.title('Test expected city minsk')
    def test_expected_city_minsk(self, browser):
        main = ShopMainPage(browser)
        main.open()
        main.expected_city_of_minsk()

    @allure.title('Testing correctness of email input')
    def testing_correctness_of_email_input(self, browser):
        main = ShopMainPage(browser)
        main.open()
        main.error_incorrect_email_input()

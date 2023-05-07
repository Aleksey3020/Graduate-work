from page_object.sign_in_and_registration import SignInAndRegistration
import allure


@allure.suite('Checking the sign in and registration section')
class TestSignInAndRegistration:
    @allure.title('Examination for errors in all fields')
    def test_error(self, browser):
        registration = SignInAndRegistration(browser)
        registration.open()
        registration.open_registration()
        registration.check_for_error()

    @allure.title('Testing correctness of email input')
    def test_email_input(self, browser):
        registration = SignInAndRegistration(browser)
        registration.open()
        registration.open_registration()
        registration.email_validation()

    @allure.title('Checking if country codes do not match')
    def test_if_country_codes_do_not_match(self, browser):
        registration = SignInAndRegistration(browser)
        registration.open()
        registration.open_registration()
        registration.checking_country_codes()

    @allure.title('Check if country codes match')
    def test_if_country_codes_match(self, browser):
        registration = SignInAndRegistration(browser)
        registration.open()
        registration.open_registration()
        registration.checking2_country_codes()

    @allure.title('Symbol count check and password visibility button')
    def test_for_the_number_of_characters_in_the_password(self, browser):
        registration = SignInAndRegistration(browser)
        registration.open()
        registration.open_registration()
        with allure.step('Password_validation'):
            registration.password_validation()
        with allure.step('Checking the password visibility button'):
            registration.password_visibility_button()

    @allure.title('Checking the authorization button')
    def test_authorization_button(self, browser):
        registration = SignInAndRegistration(browser)
        registration.open()
        registration.open_registration()
        registration.button_authorization()

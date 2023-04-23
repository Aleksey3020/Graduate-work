from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from retrying import retry


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.webdriver = driver
        self.url: str = ''

    def open_url(self, url):
        self.webdriver.get(url)
        self.webdriver.maximize_window()

    def open(self):
        self.open_url(url=self.url)

    def find_element(self, locator: tuple, timer=50) -> WebElement:
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator: tuple, timer=50):
        return WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, content, timer=10):
        input_field = WebDriverWait(self.webdriver, timer).until(
            EC.element_to_be_clickable(locator))
        input_field.clear()
        input_field.send_keys(content)

    def get_text_from_element(self, locator, timer=10):
        element = self.find_element(locator, timer)
        return element.text

    def switch_to_iframe(self, iframe_locator, timer=10):
        WebDriverWait(self, timer).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

    def switch_to_default_context(self):
        self.webdriver.switch_to.default_content()

    def accept_alert(self):
        alert_el = self.webdriver.switch_to.alert
        alert_el.accept()
        self.switch_to_default_context()

    def dismiss_alert(self):
        alert_el = self.webdriver.switch_to.alert
        alert_el.dismiss()
        self.switch_to_default_context()

    def fill_and_accept_alert(self, content):
        alert_el = self.webdriver.switch_to.alert
        alert_el.send_keys(content)
        alert_el.accept()
        self.switch_to_default_context()

    @retry(stop_max_delay=10000)
    def element_click_with_retry(self, locator, timer=30):
        return (
            WebDriverWait(self.webdriver, timer).until(
                EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}"
            )
        ).click()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.webdriver = driver
        self.url: str = ''
        self.wait = WebDriverWait(self.webdriver, timeout=20)

    def open_url(self, url):
        self.webdriver.get(url)

    def open(self):
        self.open_url(url=self.url)
        self.webdriver.maximize_window()

    def click_element(self, locator: tuple):
        return self.wait.until(ec.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, content):
        input_field = self.wait.until(ec.element_to_be_clickable(locator))
        input_field.clear()
        input_field.send_keys(content)

    def find_visible_element(self, locator: tuple) -> WebElement:
        try:
            return self.wait.until(ec.visibility_of_element_located(locator))
        except ValueError:
            return self.wait.until(ec.visibility_of_element_located(locator))

    def get_text(self, locator: tuple) -> str:
        return self.wait.until(ec.presence_of_element_located(locator)).text

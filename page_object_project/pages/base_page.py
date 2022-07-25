from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, by, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def view_basket(self):
        self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON).click()

    def input_text(self, by, locator, text):
        self.browser.find_element(by, locator).send_keys(text)

    def check_text_for_field(self, by, locator, expected_text):
        actual_text = self.browser.find_element(by, locator).text
        assert actual_text == expected_text, "Actual text {} is not equal to expected {}".format(actual_text,
                                                                                                 expected_text)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, check authorisation"

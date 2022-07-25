from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''
    product_price = ''

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_product_to_cart(self):
        self.get_product_name()
        self.get_product_price()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def assert_product_added(self):
        expected_message = self.product_name + " has been added to your basket."
        product_added_text = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_added_text == expected_message, "Expected message {} is not equal to actual {}".format(
            expected_message, product_added_text)

    def assert_basket_total_equal_product_price(self):
        expected_message = "Your basket total is now " + self.product_price
        basket_total_text = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert basket_total_text == expected_message, "Expected message {} is not equal to actual {}".format(
            expected_message, basket_total_text)

    def get_product_name(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return self.product_name

    def get_product_price(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return self.product_price

    def assert_not_success_message_appeared(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Success message was found!"

    def assert_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Success message didn't disappeared"

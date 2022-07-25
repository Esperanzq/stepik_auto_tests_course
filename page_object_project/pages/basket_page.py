from page_object_project.pages.base_page import BasePage
from page_object_project.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        url = self.browser.current_url
        assert "basket" in url, "Basket wasn't found in current url: {}".format(url)

    def should_be_basket_header(self):
        basket_header = self.browser.find_element(*BasketPageLocators.BASKET_HEADER)
        assert basket_header.is_displayed(), "Basket header wasn't found!"

    def assert_basket_has_no_items(self):
        assert not self.is_element_present(*BasketPageLocators.ITEMS_TO_BUY_HEADER), "Basket isn't empty"

    def assert_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_HEADER), "Basket is empty header wasn't found!"

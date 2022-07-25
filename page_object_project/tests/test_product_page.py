import pytest
import time
from page_object_project.pages.basket_page import BasketPage
from page_object_project.pages.login_page import LoginPage
from page_object_project.pages.main_page import MainPage
from page_object_project.pages.product_page import ProductPage

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, request):
        if "user" in request.node.name:
            email = str(time.time()) + "@fakemail.org"
            password = str(time.time())
            page = MainPage(browser, "http://selenium1py.pythonanywhere.com")
            page.open()
            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            login_page.should_be_login_page()
            login_page.register_new_user(email, password)
            login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.add_product_to_cart()
        product_page.assert_product_added()
        product_page.assert_basket_total_equal_product_price()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.add_product_to_cart()
        product_page.assert_product_added()
        product_page.assert_basket_total_equal_product_price()

    @pytest.mark.need_review
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.view_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.assert_basket_has_no_items()
        basket_page.assert_basket_is_empty()

    @pytest.mark.xfail()
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.add_product_to_cart()
        product_page.assert_not_success_message_appeared()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.assert_not_success_message_appeared()

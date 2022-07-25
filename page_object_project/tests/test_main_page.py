import pytest

from page_object_project.pages.basket_page import BasketPage
from page_object_project.pages.login_page import LoginPage
from page_object_project.pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.view_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.assert_basket_has_no_items()
        basket_page.assert_basket_is_empty()

    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.should_be_login_link()
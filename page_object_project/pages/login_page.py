from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "Login wasn't found in current url: {}".format(url)

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form.is_displayed(), "Login form wasn't found!"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form.is_displayed(), "Register form wasn't found!"

    def register_new_user(self, email, password):
        self.input_text(*LoginPageLocators.REGISTER_FORM_EMAIL_FIELD, email)
        self.input_text(*LoginPageLocators.REGISTER_FORM_PASSWORD_FIELD, password)
        self.input_text(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD_FIELD, password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

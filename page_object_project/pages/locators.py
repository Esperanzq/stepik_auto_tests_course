from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=registration-email]")
    REGISTER_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name=registration-password1]")
    REGISTER_FORM_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name=registration-password2]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".row h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_ADDED_MESSAGE = (By.XPATH, '//div[1]/div[@class="alertinner "]')
    BASKET_TOTAL_MESSAGE = (By.XPATH, '//div[3]/div[@class="alertinner "]/p[1]')


class BasketPageLocators:
    BASKET_HEADER = (By.XPATH, '//div/h1[contains(text(), "Basket")]')
    EMPTY_BASKET_HEADER = (By.XPATH, '//div/p[contains(text(), "Your basket is empty")]')
    ITEMS_TO_BUY_HEADER = (By.XPATH, '//div/h2[contains(text(), "Items to buy now")]')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "content_inner")))
    el_value = browser.find_element(By.XPATH, "//form[@id='add_to_basket_form']/button").get_attribute("value")
    required_value = "Добавить в корзину"
    assert required_value == el_value, "Found value {} is not equal to required {}".format(el_value, required_value)

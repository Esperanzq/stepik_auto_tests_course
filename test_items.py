from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "content_inner")))
    buttons = browser.find_elements(By.XPATH, "//form[@id='add_to_basket_form']/button")
    assert len(buttons) == 1, "Len: {} is not equal to required '1'".format(len(buttons))

from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_page_contains_button_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    assert button, 'There is not button "Add in basket"'
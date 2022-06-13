from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def culc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome('/home/user/environments/chromedriver')
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    browser.find_element(By.ID, 'book').click()
    
    browser.execute_script("window.scrollBy(0, 100);")

    num = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(culc(num))

    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)
    browser.quit()
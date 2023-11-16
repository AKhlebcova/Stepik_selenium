from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    element_x = browser.find_element(By.TAG_NAME, 'img')

    x = element_x.get_attribute('valuex')
    print(x)
    answer = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)
    check_el = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check_el.click()
    radio_el = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_el.click()
    but = browser.find_element(By.TAG_NAME, 'button')
    but.click()
finally:
    time.sleep(15)
    browser.quit()
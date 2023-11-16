from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://SunInJuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    answer = browser.find_element(By.ID, 'input_value').text
    input_el = browser.find_element(By.ID, 'answer')
    time.sleep(1)
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_el)
    input_el.send_keys(calc(answer))
    browser.find_element(By.ID, 'robotCheckbox').click()
    print(browser.find_element(By.CSS_SELECTOR, '[type="radio"]').get_attribute('checked'))
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()



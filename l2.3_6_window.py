from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    answer = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(answer))
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(3)
    browser.quit()





# browser.switch_to.window(window_name)
# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]
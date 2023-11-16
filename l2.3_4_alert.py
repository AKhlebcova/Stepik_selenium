from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    answer = browser.find_element(By.ID, 'input_value').text
    print(answer)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(calc(answer))
    browser.find_element(By.TAG_NAME, 'button').click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
finally:
    browser.quit()







# alert = browser.switch_to.alert
# alert.accept()
#
# alert = browser.switch_to.alert
# alert_text = alert.text
#
# confirm = browser.switch_to.alert
# confirm.accept()
# confirm.dismiss()
#
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()


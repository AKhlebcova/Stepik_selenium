from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link1 = 'https://suninjuly.github.io/selects1.html'
link2 = 'https://suninjuly.github.io/selects2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link2)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    answer = str(int(num1) + int(num2))
    print(answer)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(answer)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(15)
    browser.quit()


# select.select_by_visible_text("text") и select.select_by_index(index)

#
# select = Select(browser.find_element(By.TAG_NAME, "select"))
# select.select_by_value("1") # ищем элемент с текстом "Python"
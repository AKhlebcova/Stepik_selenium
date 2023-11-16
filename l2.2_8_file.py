import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
current_dir = os.path.abspath(os.path.dirname(__file__))
link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Ivan')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Ivanov')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Ivanov@gmail.com')
    file_path = os.path.join(current_dir, 'text.txt')
    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()


# current_dir = os.path.abspath(os.path.dirname(__file__))
# print(current_dir)
# print(os.path.dirname(__file__))

# получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
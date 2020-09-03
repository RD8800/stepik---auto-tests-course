from selenium import webdriver
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)

    fistname = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    fistname.send_keys("123")
    lastname = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    lastname.send_keys("456")
    mail = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    mail.send_keys("789@ya.ru")
    file = browser.find_element_by_css_selector('[type="file"]')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

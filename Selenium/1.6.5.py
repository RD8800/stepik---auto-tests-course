from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name('form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name('form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.third')
    input3.send_keys("blabla@gmail.com")
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()


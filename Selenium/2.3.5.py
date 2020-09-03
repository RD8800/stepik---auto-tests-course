from selenium import webdriver
import os
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    new_window = browser.window_handles[1]
    print(new_window)
    browser.switch_to.window(new_window)
    num = browser.find_element_by_id('input_value').text
    print(num)
    x = calc(num)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(x)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

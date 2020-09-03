from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x,y):
  z = int(x) + int(y)
  print(z)
  return str(z)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    x = calc(num1, num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

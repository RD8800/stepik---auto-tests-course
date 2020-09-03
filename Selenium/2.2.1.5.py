from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input2 = browser.find_element_by_id('treasure')
    x = calc(input2.get_attribute("valuex"))
    print(x)
    find_box= browser.find_element_by_id('answer')
    find_box.send_keys(x)
    input3 = browser.find_element_by_id('robotCheckbox')
    input3.click()
    input4 = browser.find_element_by_id('robotsRule')
    input4.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

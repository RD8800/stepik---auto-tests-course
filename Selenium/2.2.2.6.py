from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

num = browser.find_element_by_id('input_value').text
x = calc(num)

answer = browser.find_element_by_id("answer")
answer.send_keys(x)
button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
input3 = browser.find_element_by_id('robotCheckbox')
input3.click()
input4 = browser.find_element_by_id('robotsRule')
input4.click()
button.click()
assert True

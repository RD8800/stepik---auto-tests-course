from selenium import webdriver
import time
import unittest
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
def do_test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_class_name('form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name('form-control.third')
        input3.send_keys("blabla@gmail.com")
        button = browser.find_element_by_css_selector('button.btn')
        button.click()
        result = browser.find_element_by_css_selector('h1').text
        print(result)
        assert (result, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
    finally:
        time.sleep(5)
        browser.quit()

class TestAbs(unittest.TestCase):
    def test1(self):
        do_test(link1)

    def test2(self):
        do_test(link2)

if __name__ == "__main__":
    unittest.main()

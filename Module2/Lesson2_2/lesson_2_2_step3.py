from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

page1 = "http://suninjuly.github.io/selects1.html"
page2 = "http://suninjuly.github.io/selects2.html"

for page in [page1, page2]:
    try:
        browser = webdriver.Chrome()
        browser.get(page)

        res = 0
        for element in ["#num1", "#num2"]:
            res += int(browser.find_element_by_css_selector(element).text)

        Select(browser.find_element_by_css_selector("#dropdown")).select_by_value(str(res))

        browser.find_element_by_css_selector("button[type='submit'].btn").click()

    finally:
        time.sleep(5)
        browser.quit()

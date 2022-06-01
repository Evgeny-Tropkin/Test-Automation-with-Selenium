from selenium import webdriver
import time


link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    fields = browser.find_elements_by_tag_name("input")
    count = 0

    for field in fields:
        field.send_keys("text " + str(count))
        count = count + 1

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()

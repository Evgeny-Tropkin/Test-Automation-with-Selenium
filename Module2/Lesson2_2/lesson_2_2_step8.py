from selenium import webdriver
import os
import time


page = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(page)

    browser.find_element_by_name("firstname").send_keys("Name")
    browser.find_element_by_name("lastname").send_keys("Surname")
    browser.find_element_by_name("email").send_keys("E-mail")

    file_name = "upload.txt"
    script_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(script_dir, "lesson_2_2_step8_attachment", file_name)

    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_css_selector("button[type='submit'].btn").click()

finally:
    time.sleep(5)
    browser.quit()

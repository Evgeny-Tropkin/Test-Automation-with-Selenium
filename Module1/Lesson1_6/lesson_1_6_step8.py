from selenium import webdriver
import math
import time
import lesson_1_6_step4


if __name__ == "__main__":
    page = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome()

    try:
        browser.get(page)
        lesson_1_6_step4.complete_form(browser)
        browser.find_element_by_xpath("//button[@type='submit']").click()

    finally:
        time.sleep(10)
        browser.quit()

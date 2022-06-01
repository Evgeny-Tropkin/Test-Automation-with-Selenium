from selenium import webdriver
import math
import time
import lesson_1_6_step4


if __name__ == "__main__":
    page = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Chrome()

    try:
        browser.get(page)
        link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
        link = browser.find_element_by_link_text(link_text)
        link.click()
        lesson_1_6_step4.complete_form(browser)

    finally:
        time.sleep(10)
        browser.quit()

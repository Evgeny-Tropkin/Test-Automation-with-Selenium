from selenium import webdriver
import time


def complete_form(web_driver):
    input1 = web_driver.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = web_driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = web_driver.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = web_driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = web_driver.find_element_by_css_selector("button.btn")
    button.click()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        complete_form(browser)
    finally:
        time.sleep(15)
        browser.quit()

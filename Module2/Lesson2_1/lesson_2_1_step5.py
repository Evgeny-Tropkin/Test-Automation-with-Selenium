from selenium import webdriver
import math
import time


# в шаге 7 используется аналогичная функция, соответствующая заданию шага 7
def get_x(web_driver):
    return int(web_driver.find_element_by_id("input_value").text)


# функция, используемая так же в:
# шаге 7 урока 1 модуля 2 (данный модуль)
# шаге 6 урока 2 модуля 2
def complete_form(page_address, x_function):
    browser = webdriver.Chrome()

    try:
        browser.get(page_address)
        # get_x
        x = x_function(browser)
        y = math.log(abs(12*math.sin(x)))
        # insert answer
        browser.find_element_by_id("answer").send_keys(str(y))
        # check checkbox "I'm the robot" if it's not checked
        robot_check_box = browser.find_element_by_id("robotCheckbox")
        if not robot_check_box.is_selected():
            robot_check_box.click()
        # button clicks
        for selector in ["#robotsRule", "button.btn[type='submit']"]:
            element = browser.find_element_by_css_selector(selector)
            browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    page = "http://suninjuly.github.io/math.html"
    complete_form(page, get_x)

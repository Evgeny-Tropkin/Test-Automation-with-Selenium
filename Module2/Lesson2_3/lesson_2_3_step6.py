from selenium import webdriver
import math
import time


def calculate(str_x):
    num_x = int(str_x)
    res = math.log(math.fabs(12 * math.sin(num_x)))
    return str(res)


page1_address = "http://suninjuly.github.io/redirect_accept.html"


try:
    # 1. Открыть страницу
    browser = webdriver.Chrome()
    browser.get(page1_address)
    # 2. Нажать на кнопку
    browser.find_element_by_css_selector("button[type='submit'].trollface").click()
    # 3. Переключиться на новую вкладку
    page2 = browser.window_handles[1]
    browser.switch_to.window(page2)
    # 4. Пройти капчу для робота и получить число-ответ
    x = browser.find_element_by_id("input_value").text
    answer = calculate(x)
    browser.find_element_by_id("answer").send_keys(answer)
    # Передать ответ (нажать кнопку "Submit")
    browser.find_element_by_css_selector("button[type='submit'].btn").click()

finally:
    time.sleep(5)
    browser.quit()

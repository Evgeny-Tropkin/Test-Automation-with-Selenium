import math
import time
from selenium import webdriver


# Вычисление функции, необходимой по заданию
def calculate(str_x):
    num_x = int(str_x)
    res = math.log(math.fabs(12 * math.sin(num_x)))
    return str(res)


# Нажатие кнопки с атрибутом <type='submit'> на тестируемой странице
def submit_click(driver):
    driver.find_element_by_css_selector("button[type='submit'].btn").click()


page = "http://suninjuly.github.io/alert_accept.html"

try:
    # 1. Открыть страницу
    browser = webdriver.Chrome()
    browser.get(page)
    # 2. Нажать на кнопку
    submit_click(browser)
    # 3. Принять confirm
    browser.switch_to.alert.accept()
    # 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_id("input_value").text
    answer = calculate(x)
    browser.find_element_by_id("answer").send_keys(answer)
    submit_click(browser)

finally:
    time.sleep(5)
    browser.quit()

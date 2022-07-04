from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


def calculate(str_x):
    num_x = int(str_x)
    res = math.log(math.fabs(12 * math.sin(num_x)))
    return str(res)


page = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # 1. Открыть страницу
    browser = webdriver.Chrome()
    browser.get(page)
    # 2. Дождаться, когда цена дома уменьшится до $100
    # (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 25).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # 3. Нажать на кнопку "Book"
    browser.find_element(By.ID, "book").click()
    # 4. Решить математическую задачу
    x = browser.find_element(By.ID, "input_value").text
    result = calculate(x)
    # Отправить решение
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    browser.quit()

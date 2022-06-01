from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration2.html"
first_name = "FirstName"
last_name = "LastName"
email = "E-Mail@example.com"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input[required].first").send_keys(first_name)
    browser.find_element(By.CSS_SELECTOR, "input[required].second").send_keys(last_name)
    browser.find_element(By.CSS_SELECTOR, "input[required].third").send_keys(email)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()

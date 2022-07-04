from selenium import webdriver
import time

# enter page address
page = ""

try:
    browser = webdriver.Chrome()
    browser.get(page)
finally:
    time.sleep(5)
    browser.quit()

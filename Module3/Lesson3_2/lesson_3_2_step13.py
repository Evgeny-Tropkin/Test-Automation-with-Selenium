import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(fill_form(link), "Congratulations! You have successfully registered!")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(fill_form(link), "Congratulations! You have successfully registered!")


def fill_form(page):
    # Data for required fields
    first_name = "FirstName"
    last_name = "LastName"
    email = "E-Mail@example.com"
    browser = webdriver.Chrome()

    browser.get(page)
    # Fill required fields
    browser.find_element(By.CSS_SELECTOR, "input[required].first").send_keys(first_name)
    browser.find_element(By.CSS_SELECTOR, "input[required].second").send_keys(last_name)
    browser.find_element(By.CSS_SELECTOR, "input[required].third").send_keys(email)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)

    # return element for checking registration
    return browser.find_element(By.TAG_NAME, "h1").text


if __name__ == "__main__":
    unittest.main()

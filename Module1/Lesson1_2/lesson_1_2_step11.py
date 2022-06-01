import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# Инициализируем драйвер браузера.
# После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

time.sleep(3)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Ищем поле для ввода текста
text_area = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
text_area.send_keys("get()")
time.sleep(3)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Сообщим драйверу, что нужно нажать на найднную кнопку.
submit_button.click()
time.sleep(3)

# После выполнения всех действий закрыть окно браузера
driver.quit()

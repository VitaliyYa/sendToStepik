from selenium import webdriver
from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sendToStepik import sendToStepik
import time

# в переменную task_link вставить адрес страницы с заданием
task_link = 'https://stepik.org/lesson/165493/step/5?unit=140087'

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

# Считать значение для переменной x. Посчитать математическую функцию от x, ввести ответ в текстовое поле
x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

# Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить
for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
  browser.find_element_by_css_selector(selector).click()

# Копирование числа из алерта
alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()
answer = alert_text.split(': ')[-1]

time.sleep(1)
browser.quit()

# Отправка решения на степик
sendToStepik(task_link, answer)

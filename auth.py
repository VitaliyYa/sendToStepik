'''
Перед закидыванием ответов на задания запустить для сохранения сеанса
Сеанс сохраняется в текущей папке, в chrome-data
на авторизацию дается 30 секунд, можно изменить
'''

# Источник: http://qaru.site/questions/139850/how-to-save-and-load-cookies-using-python-selenium-webdriver

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('/usr/bin/chromedriver',options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 
driver.get('https://stepik.org/catalog?auth=login')
time.sleep(30)  # Время для авторизации
driver.quit()

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # открываем страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    #browser = webdriver.Chrome()
    # ecли путь к драйверу не задан в переменных окружения, комментируем предыдущую строчку и задаем явный путь ниже
    browser = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    #говорим Selenium проверять в течение 13 секунд пока кнопка не станет кликабельной
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    #Нажать на кнопку "Book"
    button.click()

    # Найти элемент c числовым значением
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # вводим ответ в текстовое поле и выполняем сабмит
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_xpath("//button[@type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
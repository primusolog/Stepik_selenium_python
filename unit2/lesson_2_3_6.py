from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # открываем страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    #browser = webdriver.Chrome()
    # ecли путь к драйверу не задан в переменных окружения, комментируем предыдущую строчку и задаем явный путь ниже
    browser = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    #нажать кнопку
    browser.find_element_by_xpath("//button[@type='submit']").click()

    #переключиться на на другую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
from selenium import webdriver
import time

try:
    # открываем страницу
    link = "http://suninjuly.github.io/cats.html"
    #browser = webdriver.Chrome()
    # ecли путь к драйверу не задан в переменных окружения, комментируем предыдущую строчку и задаем явный путь ниже
    browser = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    #browser.implicitly_wait(5)
    browser.get(link)
    # комментируем паузу и вместо нее добавдяем неявное ожидание implicit wait
    # time.sleep(1)

    browser.find_element_by_id("button")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
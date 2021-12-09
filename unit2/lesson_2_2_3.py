from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    # открываем страницу
    link = " http://suninjuly.github.io/selects1.html"
    #browser = webdriver.Chrome()
    # ecли путь к драйверу не задан в переменных окружения, комментируем предыдущую строчку и задаем явный путь ниже
    browser = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    # определить заданные числа
    # Посчитать сумму заданных чисел
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    value = int(num1) + int(num2)


    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(value))
    browser.find_element_by_xpath("//button[@type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
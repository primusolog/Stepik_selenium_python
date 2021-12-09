from selenium import webdriver
import time
import os

try:
    # открываем страницу
    link = "http://suninjuly.github.io/file_input.html"
    #browser = webdriver.Chrome()
    # ecли путь к драйверу не задан в переменных окружения, комментируем предыдущую строчку и задаем явный путь ниже
    browser = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys("Vasya")
    input2 = browser.find_element_by_xpath("//input[@name='lastname']")
    input2.send_keys("Pupkin")
    input3 = browser.find_element_by_xpath("//input[@name='email']")
    input3.send_keys("vp@mailbox.com")


    # получить путь текущего каталога и сформировать путь к тестовому файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    # загрузить тестовый текстовый файл
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_xpath("//button[@type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
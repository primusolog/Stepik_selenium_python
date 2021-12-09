import time
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
link = "https://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def test(link):
    try:
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        fname = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        fname.send_keys('First')
        lname = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        lname.send_keys('Last')
        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys('Last@first.com')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "вы не зарегистрированы " \
                                                                                     "или сообщение не правильное"

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)


if __name__ == "__main__":
    try:
        test(link)
        print("Тест первой страницы удачно пройден. Вы зарегистрированы.")
        test(link2)
    except NoSuchElementException:
        print("Тест по ссылке два успешно упал.")
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

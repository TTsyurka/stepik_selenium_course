from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text                      # находим текст элемента
    num2 = browser.find_element(By.ID, "num2").text                      # находим текст элемента
    answer = str(int(num1) + int(num2))                                  # вычисляем ответ

    select = Select(browser.find_element(By.TAG_NAME, "select"))         # выбираем элемент страницы список
    select.select_by_value(answer)                                       # выбираем пункт списка, по значению

    button = browser.find_element(By.XPATH, "//button[@type='submit']")  # находим кнопку
    button.click()                                                       # нажимаем кнопку

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

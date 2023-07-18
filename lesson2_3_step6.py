from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # нахожим кнопку на странице и нажимаем её
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    # переключаемся в другую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # нахожим на странице нужное начение и сохраняем его в переменную,
    # которую потом вычисляем по заданной формулеш
    valuex = browser.find_element(By.ID, "input_value").text
    y = calc(valuex)

    # находим поле ввода и отправляем туда вычисленный ответ
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # находим и нажимаем кнопку submit
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element(By.ID, "book")
button.click()

# нахожим на странице нужное начение и сохраняем его в переменную,
# которую потом вычисляем по заданной формуле
valuex = browser.find_element(By.ID, "input_value").text
y = calc(valuex)

# находим поле ввода и отправляем туда вычисленный ответ
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

# находим и нажимаем кнопку submit
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

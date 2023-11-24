from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
t = 2

time.sleep(t)
driver.execute_script("window.scrollTo(0, 400)")

try:
    dias = Select(WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "select[contains(@id,'select-demo')]"))))
    time.sleep(t)
    dias.select_by_index(2)
    time.sleep(t)
    dias.select_by_index(4)
    time.sleep(t)
    dias.select_by_index(7)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponible...")


ciudad = Select(driver.find_element(By.ID, "multi-select"))
time.sleep(t)
ciudad.select_by_index(0)
time.sleep(t)
ciudad.select_by_index(4)
time.sleep(t)
ciudad.select_by_index(7)

time.sleep(t)
driver.close()

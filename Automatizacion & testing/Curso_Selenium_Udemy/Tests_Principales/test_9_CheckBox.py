from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Dar click a los botones de check...


driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(5)
t = 5

# WebDriverWait... / Otra forma de seleccionar elememtos...
btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn.click()

btn1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 1')]")))
btn1.click()

btn2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 2')]")))
btn2.click()

btn3 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 3')]")))
btn3.click()

btn4 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 4')]")))
btn4.click()

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(t)

time.sleep(t)
btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'check1')]")))
btn.click()

time.sleep(t)
driver.close()



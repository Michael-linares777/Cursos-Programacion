from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
driver.implicitly_wait(5)
t = 1

# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "https://demo.seleniumeasy.com/input-form-demo.html")))

time.sleep(t)
first_name = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Michael Steven")

time.sleep(t)
last_name= driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]").send_keys("Linares Velasco")

time.sleep(t)
mail = driver.find_element(By.XPATH, "//input[contains(@name,'email')]").send_keys("linaresvelascomichael@gmail.com")

time.sleep(t)
phone = driver.find_element(By.XPATH, "//input[contains(@name,'phone')]").send_keys("320 569 03 06")
time.sleep(t)

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(t)

address = driver.find_element(By.XPATH, "//input[contains(@name,'address')]").send_keys("Calle 10 # 9 - 47")
time.sleep(t)
city = driver.find_element(By.XPATH, "//input[contains(@name,'city')]").send_keys("Medellin")
time.sleep(t)

state = Select(driver.find_element(By.XPATH, "//select[contains(@name,'state')]"))
state.select_by_index(10)
time.sleep(t)

zip_code = driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("05205")
time.sleep(t)

Website_name = driver.find_element(By.XPATH, "//input[contains(@name,'website')]").send_keys("Danny_Cositas.com")
time.sleep(t)

hosting = driver.find_element(By.XPATH, "//input[contains(@value,'no')]")
hosting.click()
time.sleep(t)

Project_description = driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("Mi primera practica de ¡¡¡Verdad-Verdad!!! con Selenium... ")
time.sleep(t)

send = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]")
send.click()
time.sleep(t)

time.sleep(3)
driver.close()

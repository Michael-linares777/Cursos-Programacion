from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium.webdriver.support.ui import Select


# Seleccionar varios cajones del checkBox de formas diferentes...

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t = 2

time.sleep(t)
driver.execute_script("window.scrollTo(0, 400)")


diaSelect = driver.find_element(By.XPATH,"//select[contains(@id,'select-demo')]")
ds = Select(diaSelect)

# Tres formas de Seleccionar / Index() / Valor() / Texto()...

time.sleep(t)
ds.select_by_index(1)

time.sleep(t)
ds.select_by_value("Wednesday")

time.sleep(t)
ds.select_by_visible_text("Saturday")

# Otra forma diferente de Seleccionar... 
ciudad = Select(driver.find_element(By.ID,"multi-select")) 

time.sleep(t)
ciudad.select_by_index(0)

time.sleep(t)
ciudad.select_by_index(4)

time.sleep(t)
ciudad.select_by_index(7)


time.sleep(t)
driver.close()  
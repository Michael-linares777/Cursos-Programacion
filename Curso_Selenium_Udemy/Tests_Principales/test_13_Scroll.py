from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# Desplazamiento exacto.. / Se va directamente al elemento seleccionado...
# driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", buscar)


driver = webdriver.Chrome()
driver.get("https://pixabay.com/es/")
driver.maximize_window()
t = 2

try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    buscar = driver.find_element(
        By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    # AQUI...
    ir = driver.execute_script(
        "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", buscar)
    # ir = driver.execute_script("arguments[0].scrollIntoView();", buscar) # AQUI...

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponoible")


time.sleep(t)
driver.close()

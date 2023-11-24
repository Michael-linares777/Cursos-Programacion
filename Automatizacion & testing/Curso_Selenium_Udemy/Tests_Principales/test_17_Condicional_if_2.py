from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Validar con el condicional if / (is_enabled & is_displayed)...

t = 1
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)
driver.execute_script("window.scrollTo(0, 350)")

try:
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id,'submit')]")))
    element = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
    print(element.is_enabled()) # (enabled = "habilitar" o "permitir") Un booleano con el que verifico que el elemento o botón si esté activo...
    print('La operacion fue exitosa...')

    if(element.is_enabled() == True):
        print('Puedes dar click...')
    else:
        print('No puedes dar click...')

except TimeoutException as ex:
    print(ex.msg)
    print('Algo salio mal al ejecutar la funcion...')

btn = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
print(btn.is_enabled())

if btn.is_enabled() == True:
    print("Puedes dar click...")
else:
    print("No puedes dar click...")


time.sleep(t)
driver.close()

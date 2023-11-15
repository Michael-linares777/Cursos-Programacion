from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# Validar campos no completados...

t = 2
driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(t)

# Dar click al boton de enviar (send)...
btn = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]")
btn.click()
time.sleep(t)

# Validar campo de texto / first name....
first_name = value_first = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
# Guardar el texto y almacenarlo en una variable...
name = first_name.text
print(f"El valor del error es: {name}")

# # Iteramos sobre el campo de first name... Campo no valido...
# if name == "Please supply your first name":
#     print("Falta el nombre...")
# else:
#     print("Nombre correcto...")

# Iteramos sobre el campo de first name... Campo valido...
if name == "Please supply your first name":
    nombre_campo = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Michael...")
    print("Nombre correcto...")
else:
    print("Falta el nombre...")

# Validar el estado del boton send... 
print(btn.is_enabled())
if btn.is_enabled() == False: # (is_enabled()) / (enabled = "habilitar" o "permitir") Un booleano con el que verifico que el elemento o botón si esté activo...
    print("Faltan campos por llenar...")
else:
    print("Todo listo... OK")



time.sleep(t)
driver.close()
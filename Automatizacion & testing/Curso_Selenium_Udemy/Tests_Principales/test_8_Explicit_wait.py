from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Explicit Wait:
# El Explicit Wait es una espera específica que se aplica a un elemento en particular y se utiliza cuando se necesita
# esperar por condiciones específicas antes de interactuar con un elemento.Permite definir condiciones personalizadas
# para esperar, como esperar a que un elemento esté visible o tenga un cierto valor antes de continuar.
# Es más flexible que el Implicit Wait porque puedes personalizar las condiciones de espera.

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()
# driver.implicitly_wait(10)
t = 2

# Ejemplo de explicit_wait()...
# Ejercicio no funcional / es solo para ver la sintaxis... / No se abre el elemento...
# -------------------------------------------------------------------------------------------------
# wait = WebDriverWait(driver, 10)  # Espera explícita de 10 segundos
# elemento = wait.until(EC.presence_of_element_located((By.ID, "mi_elemento")))
# -------------------------------------------------------------------------------------------------
# btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "myDynamicElement")))
# btn1.click()

time.sleep(t)
mensaje = driver.find_element(
    By.XPATH, "//input[contains(@id,'user-message')]").send_keys("Michael Linares" + Keys.TAB + Keys.ENTER)

# driver.find_element(By.XPATH,"//input[contains(@id,'value1')]").send_keys(7)
# driver.find_element(By.XPATH,"//input[contains(@id,'value2')]").send_keys(7)
# driver.find_element(By.XPATH,"//button[@type='button'][contains(.,'Get Total')]").click()
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@id,'value1')]").send_keys(
    "7" + Keys.TAB + "7" + Keys.TAB + Keys.ENTER)
# Lo mismo pero solo en una linea de codigo...

time.sleep(t)
driver.close()

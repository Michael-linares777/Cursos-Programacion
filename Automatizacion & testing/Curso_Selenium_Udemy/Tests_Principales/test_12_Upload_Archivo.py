from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException 

driver = webdriver.Chrome()
driver.get("https://testpages.eviltester.com/styled/file-upload-test.html")
driver.maximize_window()
t = 1
time.sleep(t)

# Validar por Try-catch...
try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@type,'file')]"))) # Validar con explicit_wait que el elemento exista..
    buscar = driver.find_element(By.XPATH, "//input[contains(@type,'file')]") # Escojer elementos...
    buscar.send_keys(r"C:\Users\Administrador\Desktop\Cursos Programacion\Imagenes\Cursos.png") # Escribir ruta de archivo...
    time.sleep(.5)
    driver.find_element(By.XPATH, "//label[@for='itsanimage'][contains(.,'Image')]").click() # Seleccionar elemento y dar click...
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click() # Seleccionar elemento y dar click...

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponoible")


time.sleep(t)
driver.close()









from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# Validar con Alert y ventanas modales....

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
t = 1


# time.sleep(t)
# driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
# time.sleep(t)
# driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
# time.sleep(t)
# driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
# time.sleep(t)
# driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]").click()


# SIEMPRE ES MEJOR TRABAJAR CON UN TRY-CATCH... SON MEJORES PRACTICAS DE PROGRAMACIÓN...


driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)

try:
    buscar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[5]")))
    buscar = driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    print("La operación fue exitosa...")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("Algo salio mal al ejecutar la función...")


time.sleep(1)
driver.close()

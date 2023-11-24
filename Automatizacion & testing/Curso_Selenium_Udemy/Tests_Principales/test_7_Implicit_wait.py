from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# .implicit_wait(10) / Es un tiempo de espera... / para darle al navegador oportunidad de ejecutar si existen errores...
# El Implicit Wait es una espera global que se aplica a todos los elementos del WebDriver durante toda la sesión.
# Se utiliza principalmente para establecer un tiempo de espera predeterminado para todos los elementos.

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)

t = 1
time.sleep(t)

nom = driver.find_element(
    By.XPATH, "//input[contains(@id,'userName')]").send_keys("Michael")
time.sleep(t)

# Modificamos la dirección... "tiene un error" / Para ensayar el driver.implicitly_wait(10)...
mail = driver.find_element(By.XPATH, "input[@id='userEmail']")
mail.send_keys("Linaresvelascomichael@gmail.com")
time.sleep(t)

direccion = driver.find_element(
    By.XPATH, "//textarea[contains(@id,'currentAddress')]")
direccion.send_keys("Calle 10 # 9 - 47")
time.sleep(t)

driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

t = 1
driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

# Scroll hacia abajo
driver.execute_script('window.scrollTo(0, 500)')

try:
    # Espera a que el botón sea clickeable
    btn_send = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Send')]")))
    btn_send.click()

    # Espera a que el texto de error sea visible
    texto_first_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")))
    valor_error = texto_first_name.text

    print(f"El valor del error del campo first_name es: {valor_error}... 'Por favor proporcione su nombre'...")

    if valor_error == 'Please supply your first name':
        # Espera a que el campo de nombre sea visible y luego lo encuentra
        campo_nombre = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@name,'first_name')]")))
        campo_nombre.send_keys("Michael")
        print('Nombre correcto...')
    else:
        print('Falta el nombre...')

    print('La operación fue exitosa...')

except TimeoutException as ex:
    print(f"Tiempo de espera excedido al buscar el elemento: {ex}")
    print('Algo salió mal al ejecutar la función...')

finally:
    time.sleep(t)
    driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
t = 1

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

try:
    # Obteniendo todos los links de la página...
    links = driver.find_elements(By.TAG_NAME, "a")
    print(
        f"El número de links que hay en la página es de: {len(links)} links...")
    time.sleep(2)

    # Hacemos un bucle for para enumerar y mostrar todos los links de la página con sus respectivos titulos...
    for indice, link in enumerate(links):
        print(f"{indice}: Titulo: {link.text}... Links: {link}")

    print(f"La operación fue exitosa: {len(links)} links...")
    time.sleep(t)


except TimeoutException as ex:
    print(ex.msg)
    print("Algo salió mal al ejecutar la función.")


driver.find_element(
    By.XPATH, "(//a[@href='#'][contains(.,'Date pickers')])[1]").click()
time.sleep(t)

driver.find_element(
    By.XPATH, "(//a[@href='./jquery-date-picker-demo.html'][contains(.,'JQuery Date Picker')])[1]").click()
time.sleep(t)


time.sleep(t)
driver.close()

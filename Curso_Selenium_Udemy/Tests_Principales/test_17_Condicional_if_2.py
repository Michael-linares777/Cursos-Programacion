from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# Validar con el condicional if / (is_enabled & is_displayed)...

t = 1
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)
driver.execute_script("window.scrollTo(0, 350)")

btn = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
print(btn.is_enabled()) # (enabled = "habilitar" o "permitir") Un booleano con el que verifico que el elemento o botón si esté activo...

if btn.is_enabled() == True:
    print("Puedes dar click...")
else:
    print("No puedes dar click...")


time.sleep(t)
driver.close()

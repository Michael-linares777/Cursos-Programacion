from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# Validar con el condicional if / (is_enabled & is_displayed)...

t = 2 
driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(t)

try:
    titulo = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//img[@src='/images/Toolsqa.jpg']")))
    titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
    print(titulo.is_displayed())
    btn1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    
    if titulo.is_displayed() == True:
        print("La imagen existe...")
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(t)
        btn1.click()
        time.sleep(t)
        print("La operacion fue exitosa...")

    else:
        print("La imagen no existe...")

except TimeoutException as ex:
    print(ex.msg)
    print("Algo salio mal al ejecutar la funcion...")

time.sleep(t)
driver.close()
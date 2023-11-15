from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# AUTOMATIZAR Y CONTROLAR ELEMENTOS POR XPATH... / CON LA FUNCIÓN By...

# Inicializar el navegador...
driver = webdriver.Chrome()

# Abrir Pagina...
driver.get("https://demoqa.com/text-box")

# Maximizar la pantalla...
driver.maximize_window()

# Para aplicar tiempos de espera...
time.sleep(1)


# Buscar elementos por selector específico...
nom = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
nom.send_keys("Michael")
time.sleep(1)

mail = driver.find_element(By.XPATH, "//input[@id='userEmail']")
mail.send_keys("Linaresvelascomichael@gmail.com")
time.sleep(1)

direccion = driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]")
direccion.send_keys("Calle 10 # 9 - 47")
time.sleep(1)

# Para automatixar el desplazamiento hacia abajo / Con un sistema de scroll de JavaScrip...
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(1)

direccion_2 = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
direccion_2.send_keys("Calle 30 # 80 - 110")
time.sleep(1)

# Para seleccionar y hacer clic en los botones...
boton = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
boton.click()
time.sleep(2)

# Cerrar el navegador...
driver.close()

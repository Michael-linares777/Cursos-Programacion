from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# AUTOMATIZAR Y CONTROLAR ELEMENTOS POR ID... CON LA FUNCIÓN By...

# Inicializar el navegador...
driver = webdriver.Chrome()

# Abrir Pagina...
driver.get("https://demoqa.com/text-box")

# Maximizar la pantalla...
driver.maximize_window()

# Para aplicar tiempos de espera...
time.sleep(2)

# Buscar elementos por selector específico / Con ID...
nom = driver.find_element(By.ID,"userName")
nom.send_keys("Michael")
time.sleep(2)

mail = driver.find_element(By.ID,"userEmail")
mail.send_keys("Linaresvelascomichael@gmail.com")
time.sleep(2)

direccion = driver.find_element(By.ID,"currentAddress")
direccion.send_keys("Calle 10 # 9 - 47")
time.sleep(1)

# Para automatixar el desplazamiento hacia abajo / Con un sistema de scroll de JavaScrip...
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(2)

direccion_2 = driver.find_element(By.ID,"permanentAddress")
direccion_2.send_keys("Calle 30 # 80 - 110")
time.sleep(2)

# Seleccionar y dar click en los botones...
boton = driver.find_element(By.ID,"submit")
boton.click()
time.sleep(2)


# Cerrar el navegador
driver.close()
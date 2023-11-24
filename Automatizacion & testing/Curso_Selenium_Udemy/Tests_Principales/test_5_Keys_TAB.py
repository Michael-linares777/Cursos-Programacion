from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# CREANDO SCRIPTS CON LA FUNCIÓN KEYS...

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

element = driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
element.send_keys("Michael")
element.send_keys(Keys.TAB + "LinaresVelascoMichael@gmail.com" + Keys.TAB + "Calle 10 # 9 - 47" + Keys.TAB + "Calle 30 # 80 - 110" + Keys.TAB + Keys.ENTER)
time.sleep(1)

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(1)

driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

# llenando un formulario con Unittest...

t = 2

class PruebaLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)  # Se establece un tiempo máximo de espera de 10 segundos
    
    def test_login_1(self):
        try:
            with self.driver as driver:
                driver.get("https://www.saucedemo.com/")
                driver.maximize_window()
                name = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'user-name')]")))
                name.send_keys("Michael")
                password = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'password')]")))
                password.send_keys("admin123")
                button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'login-button')]")))
                button.click()
                error = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(@data-test,'error')]")))
                error_text = error.text
                error_español = "Epic sadface: El nombre de usuario y la contraseña no coinciden con ningún usuario en este servicio..."
                if error_text == "Epic sadface: Username and password do not match any user in this service":
                    print(f"Los datos son incorrectos...{error_text}... \n{error_español} \nPrueba uno OK...")

        except Exception as e:
            self.fail(f"Ocurrió un error: {e}")


    def test_login_2(self):
        try:
            with self.driver as driver:
                driver.get("https://www.saucedemo.com/")
                driver.maximize_window()
                name = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]").send_keys("")
                password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("admin123")
                button = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]").click()
                error = self.driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
                error = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error'][contains(.,'Epic sadface: Username is required')]")
                error = error.text
                error_español = "Cara triste épica: se requiere nombre de usuario..."
                if error == "Epic sadface: Username is required":
                    print(f"Falta el Nombre...{error}... \n{error_español} \nPrueba dos OK...")
                

        except Exception as e:
            self.fail(f"Ocurrió un error: {e}")


    def tearDown(self): 
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
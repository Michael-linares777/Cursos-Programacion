from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# llenando un formulario con Unittest...

t = 1

class PruebaLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login1(self): # Siempre por convención en unittest, los métodos de prueba deben comenzar con la palabra "test". 
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        name = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]").send_keys("Michael")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("admin123")
        button = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]").click()
        error = self.driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos son incorrectos...\nPrueba uno OK...")
        time.sleep(t)



    def test_login2(self): # Siempre por convención en unittest, los métodos de prueba deben comenzar con la palabra "test". 
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        name = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]").send_keys("")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("admin123")
        button = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]").click()
        error = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        if error == "Epic sadface: Username is required":
            print("Falta el Nombre...\nPrueba dos OK...")
        time.sleep(t)


    def test_login3(self): # Siempre por convención en unittest, los métodos de prueba deben comenzar con la palabra "test". 
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        name = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]").send_keys("michael")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("")
        button = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]").click()
        error = self.driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        if error == "Epic sadface: Password is required":
            print("Falta el Password...\nPrueba tres OK...")
        time.sleep(t)
    
    
    def test_login4(self): # Siempre por convención en unittest, los métodos de prueba deben comenzar con la palabra "test". 
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        name = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]").send_keys("")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("")
        button = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]").click()
        error = self.driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        if error == "Epic sadface: Username is required":
            print("Falta Nombre & Password...\nPrueba cuatro OK...")
        time.sleep(t)
        

    def test_login5(self): # Siempre por convención en unittest, los métodos de prueba deben comenzar con la palabra "test". 
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        name = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]").send_keys("standard_user")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("secret_sauce")
        button = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]").click()
        elemento = self.driver.find_element(By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]")
        print(f"El elemento == {elemento.is_enabled()}")
        
        time.sleep(t)


    def tearDown(self):
        self.driver.close()
        time.sleep(t)


if __name__ == "__main__":
    unittest.main() 
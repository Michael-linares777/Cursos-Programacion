from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from functions.funciones import FunctionsFunciones

#  Creando la funcion click_id_valida()...

t = 1

class BaseTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome()

    def test_funcion(self):
        driver = self.driver
        prueba = FunctionsFunciones(driver)
        prueba.navegar("https://www.saucedemo.com/", t)
        prueba.texto_id_valida("user-name", "michael", t)
        prueba.texto_id_valida("password", "admin123", t)
        prueba.click_id_valida("login-button", t)

    def tearDown(self): 
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main()
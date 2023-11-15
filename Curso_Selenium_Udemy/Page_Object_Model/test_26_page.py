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

# Mejorando la funcion texto_xpath()...

t = 4

class BaseTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome()

    def test_funcion(self):
        driver = self.driver
        prueba = FunctionsFunciones(driver)
        prueba.navegar("https://www.saucedemo.com/", t)
        prueba.texto_xpath_valida("//input[@id='user-name']", "Michael", t)
        prueba.texto_xpath_valida("//input[@id='password']", "admin123", t)
        
    # Error a proposito para validar la funcion... //input[@id='user-name']"
    # def test_funcion(self):
    #     driver = self.driver
    #     t = FunctionsFunciones(driver)
    #     t.navegar("https://www.saucedemo.com/", t)
    #     t.texto_xpath_valida("//input[@id='user-nameNAME']", "Michael", t)

    def tearDown(self): 
        driver = self.driver
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

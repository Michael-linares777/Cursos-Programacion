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

# Haciendo algunos ejempos con clases...

t = 2

class BaseTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome()

    def test_funcion(self):
        driver = self.driver
        f_saludo = FunctionsFunciones(driver)
        f_saludo.saludar() 
        f_saludo.saludar2() 

    def tearDown(self): 
        driver = self.driver
        self.driver.close()
        time.sleep(t)

if __name__ == "__main__":
    unittest.main()
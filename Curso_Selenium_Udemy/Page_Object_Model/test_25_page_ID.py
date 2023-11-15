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

# llamando desde el metodo texto_id() por el ID desde el modulo de funciones...

class BaseTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome()

    def test_funcion(self):
        driver = self.driver
        t = FunctionsFunciones(driver)
        t.navegar("https://www.saucedemo.com/", 1)
        t.texto_id("user-name", "Michael", 2)
        t.texto_id("password", "admin123", 2)

    def tearDown(self): 
        driver = self.driver
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

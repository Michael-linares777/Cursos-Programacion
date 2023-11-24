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

# Incorporando la función tiempo... time.tiempo(5)

class BaseTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome()

    def test_funcion(self):
        driver = self.driver
        time = FunctionsFunciones(driver)
        time.navegar("https://www.saucedemo.com/")
        time.tiempo(5)
        

    def tearDown(self): 
        driver = self.driver
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
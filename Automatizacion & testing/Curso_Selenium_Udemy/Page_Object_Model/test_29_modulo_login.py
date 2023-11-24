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
from functions.modulo_login import PaginaLogin

#  Reutilzando codigo ...
#  Importando de dos modulos diferentes ...

tg = 1

class BaseTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome()
        t = 1


    def test_funcion(self):
        driver = self.driver
        prueba = FunctionsFunciones(driver)
        pagina = PaginaLogin(driver)
        pagina.login_master("Michael", "abcd1234", tg)
        

    def tearDown(self): 
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main()

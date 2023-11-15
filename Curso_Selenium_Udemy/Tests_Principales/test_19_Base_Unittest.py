from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# Creando clases para pruebas unitarias con Unittest...

t = 2

class BaseTest(unittest.TestCase):

    def setUp(self): # Función inicial con Unittest...
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    # Aquí puedes realizar tus pruebas utilizando self.driver
    def test1(self):
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.maximize_window()
        time.sleep(t)

    def tearDown(self): # Función final o de cierre con Unittest...
        self.driver.close()
        time.sleep(t)

if __name__ == "__main__":
    unittest.main()

'''Esta estructura se utiliza comúnmente en archivos de prueba de unidades para que las pruebas se ejecuten solo cuando ejecutas el archivo
directamente, no cuando lo importas como un módulo en otro programa. Esto es útil porque te permite definir y ejecutar pruebas unitarias
sin que se ejecuten automáticamente cuando importas el módulo en otros programas.'''

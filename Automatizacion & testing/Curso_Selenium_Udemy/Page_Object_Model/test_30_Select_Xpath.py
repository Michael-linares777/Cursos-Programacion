from selenium import webdriver
import unittest
from functions.funciones import FunctionsFunciones


# Utilizando la función Select / por Xpath...

tg = 2


class BaseTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome()

    def test_funcion(self):
        driver = self.driver
        prueba = FunctionsFunciones(driver)
        prueba.navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", tg)
        prueba.selec_xpath_text("//select[contains(@id,'select-demo')]", "Sunday", tg)

    def tearDown(self):
        driver = self.driver 
        driver.close()


if __name__ == "__main__":
    unittest.main()

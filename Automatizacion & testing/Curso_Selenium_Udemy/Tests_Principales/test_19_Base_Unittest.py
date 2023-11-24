from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

t = 2

# Creando clases para pruebas unitarias con Unittest...
class BaseTest(unittest.TestCase):

    def setUp(self): # Función inicial con Unittest...
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    # Aquí puedes realizar tus pruebas utilizando self.driver
    def test1(self):
        try:
            with self.driver as driver:
                driver.get("https://demo.seleniumeasy.com/")
                driver.maximize_window()
                # Utiliza esperas explícitas en lugar de time.sleep
                WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, "//tu/xpath/aqui")))
                # Aquí puedes realizar tus pruebas utilizando driver

        except Exception as e:
            self.fail(f"Ocurrió un error: {e}")

    def tearDown(self): # Función final o de cierre con Unittest...
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

'''Esta estructura se utiliza comúnmente en archivos de prueba de unidades para que las pruebas se ejecuten solo cuando ejecutas el archivo
directamente, no cuando lo importas como un módulo en otro programa. Esto es útil porque te permite definir y ejecutar pruebas unitarias
sin que se ejecuten automáticamente cuando importas el módulo en otros programas.'''
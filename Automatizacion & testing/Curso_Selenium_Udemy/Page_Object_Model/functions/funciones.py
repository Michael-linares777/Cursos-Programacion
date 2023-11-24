import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class FunctionsFunciones():

    def __init__(self, driver):
        self.driver = driver

    def saludar(self):
        print("Bienvenido a Page Object Model...")

    def saludar2(self):
        print("Esté es el segundo saludo...")

    def tiempo(self, tmp):
        t = time.sleep(tmp)
        return t

    def navegar(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Página abierta: {str(url)} OK.")
        t = time.sleep(tiempo)
        return t

    def texto_xpath(self, ruta_xpath,texto, tiempo):
        valor = self.driver.find_element(By.XPATH, ruta_xpath)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(tiempo)
        return t

    def texto_xpath_valida(self, ruta_xpath, texto, tiempo):
        try:
            valor = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ruta_xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, ruta_xpath)
            valor.clear()
            valor.send_keys(texto)
            print(f"Escribiendo en el campo: {ruta_xpath} El texto => {texto}")
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontro el elemento: {ruta_xpath}")

    def click_xpath_valida(self, ruta_xpath, tiempo):
        try:
            valor = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ruta_xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, ruta_xpath)
            valor.click()
            print(f"Damos click en el campo: {ruta_xpath} OK.")
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontro el elemento: {ruta_xpath}")
    
    def texto_id(self, ruta_id,texto, tiempo):
        valor = self.driver.find_element(By.ID, ruta_id)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(tiempo)
        return t
    
    def texto_id_valida(self, ruta_id,texto, tiempo):
        try:
            valor = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ruta_id)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, ruta_id)
            valor.clear()
            valor.send_keys(texto)
            print(f"Escribiendo en el campo: {ruta_id} el texto {texto}")
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontro el elemento: {ruta_id}")

    def click_id_valida(self, ruta_id,tiempo):
        try:
            valor = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ruta_id)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, ruta_id)
            valor.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontro el elemento: {ruta_id}")

    def salida(self):
        print("Se termina la prueba exitosamente...")

    def selec_xpath_text(self, ruta_xpath , texto, tiempo):
        try:
            valor = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ruta_xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, ruta_xpath)
            valor = Select(valor)
            valor.select_by_visible_text(texto)
            print(f"El campo seleccionado es: => {texto}")
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontro el elemento: {ruta_xpath}")
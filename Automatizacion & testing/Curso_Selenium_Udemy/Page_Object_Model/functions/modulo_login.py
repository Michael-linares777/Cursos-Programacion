import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from functions.funciones import FunctionsFunciones


class PaginaLogin():

    def __init__(self, driver):
        self.driver = driver

    def login_master(self, name, clave, t):
        driver = self.driver
        prueba = FunctionsFunciones(driver)
        prueba.navegar("https://www.saucedemo.com/", t)
        prueba.texto_xpath_valida("//input[@id='user-name']", name, t)
        prueba.texto_xpath_valida("//input[@id='password']", clave, t)
        prueba.click_xpath_valida("//input[@id='login-button']", t)
        prueba.salida()


from selenium import webdriver
import time

# NAVEGAR POR DIFERENTES PAGINAS....

t = 2

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://docs.python.org/3/")
driver.maximize_window()
time.sleep(t)

driver.get("https://codigo369.com/frase-galleta")
driver.maximize_window()
time.sleep(7)

# driver.back()
# time.sleep(2)

# Para devolver una pagina... /  Navegar entre paginas /
# Tambien se puede usar .back() / pero es mejor usar el _script de javascript...

# Driver.back() / Devolver todas las paginas vistas, una X una...

# Mejor usar el script / ya que con .back() las devuelve pero no se detiene, con el script
# podemos parar en una pagina, realizar una acción y continuar devolviendo las paginas..

driver.execute_script("window.history.go(-1)")
time.sleep(t)

# El -1 significa que se devuelva una pagina...
driver.execute_script("window.history.go(-1)")
time.sleep(t)

# El 2 significa que avance 2 paginas...
driver.execute_script("window.history.go(2)")

driver.close()

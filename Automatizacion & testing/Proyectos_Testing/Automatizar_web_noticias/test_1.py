from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

# Concertir archivo.py en archivo .exe / Osea un archivo ejecutable...
aplicacion_ruta = os.path.dirname(sys.executable)

# Crear una variable de tiempo
ahora = datetime.now()
mes_dia_anio = ahora.strftime("%m%d%Y")  # mmddYYYY

driver = webdriver.Chrome()

# Abrir pagina en segundo plano...
options = Options()
options.add_argument('--headless')

# driver = webdriver.Chrome(options=options)
driver.get("https://www.thesun.co.uk/sport/football/")

containers = driver.find_elements(by="xpath", value="//div[@class='teaser__copy-container']")

titulos = []
subtitulos = []
links = []

for container in containers:
    titulo = container.find_element(by="xpath", value='./a/span').text
    subtitulo = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titulos.append(titulo)
    subtitulos.append(subtitulo)
    links.append(link)

mi_diccionario = {" titulo": titulos, "subtitulo": subtitulos, "link": links}
mi_df = pd.DataFrame(mi_diccionario)

nombre_archivo = f'noticias_{mes_dia_anio}.csv'
ruta_final = os.path.join(aplicacion_ruta, nombre_archivo)

mi_df.to_csv(ruta_final)

driver.quit()

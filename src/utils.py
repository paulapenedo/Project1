from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

import shutil

import glob
from zipfile import ZipFile
from pathlib import Path
import time

from dotenv import load_dotenv
load_dotenv()



def descargar_zip():
    """Funcion que descarga el zip
    haciendo WebScrapping del boton de 'Download'
    """

    # Llamamos al driver de la web
    service = Service(executable_path="chromedriver.exe")
    #Si tienes el ejecutable en otra ubicación escribe su ruta completa: "C:/Users/User/Downloads/chromedriver.exe" . En Windows cambia los `\` por `/`

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(os.getenv('URL_WEB'))

        time.sleep(2)

        boton = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/a")

        # Clicamos el boton
        boton.click()

        time.sleep(5)

    #ruta_fichero = "C:/Users/paula/Downloads/wine+quality.zip"

        while not os.path.exists(os.getenv('PATH_ORIGEN')):
            print("Esperando a que termine la descarga")
            time.sleep(1)
            # Cerramos el driver
            #driver.quit()
        print("Archivo descargado")

    finally:
        time.sleep(2)
        driver.close()

    return "Descarga completada"






def mover_zip():
    ruta_inicial = os.getenv('PATH_ORIGEN')
    ruta_final = os.getenv('PATH_DESTINO')

    if os.path.exists(ruta_inicial):
        shutil.move(ruta_inicial, ruta_final)

    return "Listo"




def descomprimir_zip():
    # Comprobamos que existe la carpeta data y si no la creamos
    if not os.path.exists("./data"):
        os.mkdir("./data")

    # Comprobamos que el la carpeta actual del proyecto hay un zip
    path = os.getcwd()
    files = glob.glob('*.zip')

    index = 0
    for i in range(0, len(files)):
        with ZipFile(files[index], mode='r') as zip:
            data = zip.extractall(path="./data")        
        index += 1

    return "Completado"
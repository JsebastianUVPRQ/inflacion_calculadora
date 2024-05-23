from selenium import webdriver
from selenium.webdriver.opera.service import Service as OperaService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura la ubicación del OperaDriver
opera_driver_path = '/home/jsebastianp/Downloads/operadriver_linux64'

# Inicializa el servicio de OperaDriver
opera_service = OperaService(opera_driver_path)

# Configura las opciones del navegador Opera
opera_options = webdriver.ChromeOptions()
opera_options.binary_location = '/usr/lib/x86_64-linux-gnu/opera/'

# Inicializa el navegador Opera
driver = webdriver.Opera(service=opera_service, options=opera_options)

try:
    # Abre la página web
    driver.get('https://sitios.dane.gov.co/ipc/visorIPC/')

    # Espera a que el contenido se cargue (puede que necesites ajustar esto según el contenido dinámico)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    # Extrae el contenido deseado (ajusta los selectores según sea necesario)
    data_element = driver.find_element(By.CSS_SELECTOR, 'selector_de_elemento')
    print(data_element.text)

finally:
    # Cierra el navegador
    driver.quit()

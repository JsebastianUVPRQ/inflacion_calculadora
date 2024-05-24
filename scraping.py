from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura la ubicación del GeckoDriver
gecko_driver_path = '/home/jsebastianp/Downloads/drivers_browser/geckodriver'

# Inicializa el servicio de GeckoDriver
firefox_service = FirefoxService(gecko_driver_path)

# Configura las opciones del navegador Firefox (opcional)
firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument('--headless')  # Ejecución en segundo plano (sin abrir ventana del navegador)

# Inicializa el navegador Firefox
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

try:
    # Abre la página web
    driver.get('https://sitios.dane.gov.co/ipc/visorIPC/')

    # Espera a que el contenido se cargue (ajusta el tiempo según sea necesario)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Intenta encontrar el elemento deseado
        try:
            # Ajusta el selector al elemento que deseas encontrar
            data_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'selector_de_elemento'))
            )
            print(data_element.text)
        except NoSuchElementException:
            print("No se encontró el elemento especificado en la página.")
        except TimeoutException:
            print("Se agotó el tiempo de espera para encontrar el elemento.")
    except TimeoutException:
        print("Se agotó el tiempo de espera para cargar el contenido de la página.")

finally:
    # Cierra el navegador
    driver.quit()

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
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    # Extrae el contenido deseado (ajusta los selectores según sea necesario)
    # Por ejemplo, si quieres extraer una tabla:
    data_element = driver.find_element(By.CSS_SELECTOR, 'selector_de_elemento')
    print(data_element.text)

finally:
    # Cierra el navegador
    driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException

driver = webdriver.Firefox()     #Define el navegador a utilizar
driver.maximize_window()        #Maximizar ventana

for page in range(1,4):
    driver.get(f'https://www.unimarc.cl/desayuno-y-dulces/cereales?page={page}')
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scrollear toda la pagina, para que termine de cargar
    driver.execute_script("window.scrollTo(0, 0);") #Scrollear hacia arriba

    #Productos
    wait = WebDriverWait(driver, 100)   #Espera a que la pagina cargue o se demore 100 segundos
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'product-item'))) #Espera hasta que hayan cargado todas las "tarjetas" de produtos

    products = driver.find_elements(By.CLASS_NAME,'product-item') #Buscar "tarjeta" de cada producto
    for product in products:
        name = product.find_element(By.CLASS_NAME,'product-title').text     #Extrae el nombre de cada producto
        brand = product.find_element(By.CLASS_NAME,'brand-name').text       #Extrae la linea de cada producto
        price_per_kg = product.find_element(By.CLASS_NAME,'product-price-un').text
        try:
            price = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'product-price-normal'))).text #Extrae el precio de producto, con la condicion de esperar max 3 segundos - Productos precio normal
        except TimeoutException or NoSuchElementException:
            try:
                original_price = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'product-list-price'))).text #Extrae el precio sin rebajas del producto en oferta
                sale = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'product-ahorras'))).text #Extrae el precio sin rebajas del producto en oferta
                price = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'product-price'))).text #Extrae el precio de producto, con la condicion de esperar max 3 segundos - Productos bajados de precio
            except TimeoutException or NoSuchElementException:
                price = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'product-ahorras-mxn'))).text #Extrae el precio de producto, con la condicion de esperar max 3 segundos - Productos precio promocional
        print(f'Nombre: {name}\nMarca: {brand}\nPrecio original: {original_price if original_price!="" else "No aplica"}\nPrecio: {price}\nAhorras: {sale if sale!="" else "No aplica"}\nPrecio por kg: {price_per_kg}\n')   #Genera print con los datos extaidos
        original_price = ""
        sale = ""
        sleep(1)
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException


link='https://www.unimarc.cl/desayuno-y-dulces/cereales'    #Enlace a la pagina scrappear
driver = webdriver.Safari()     #Define el navegador a utilizar
driver.maximize_window()        #Maximizar ventana
#driver.implicitly_wait(10)      #Espera como maximo 20 segundos para que cargue la pagina
driver.get(link)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scrollear toda la pagina, para que termine de cargar


#Productos
wait = WebDriverWait(driver, 100)   #Espera a que la pagina cargue o se demore 100 segundos
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'product-item'))) #Espera hasta que hayan cargado todas las "tarjetas" de produtos

products = driver.find_elements(By.CLASS_NAME,'product-item') #Buscar "tarjeta" de cada producto
for product in products:
    name = product.find_element(By.CLASS_NAME,'product-title').text     #Extrae el nombre de cada producto
    brand = product.find_element(By.CLASS_NAME,'brand-name').text       #Extrae la linea de cada producto
    try:
        price = WebDriverWait(product,2).until(EC.presence_of_element_located((By.CLASS_NAME,'product-price'))).text #Extrae el precio de producto, con la condicion de esperar max 2 segundos - Productos bajados de precio
    except TimeoutException or NoSuchElementException:
        try:
            price = WebDriverWait(product,2).until(EC.presence_of_element_located((By.CLASS_NAME,'product-price-normal'))).text #Extrae el precio de producto, con la condicion de esperar max 2 segundos - Productos precio normal
        except TimeoutException or NoSuchElementException:
            print("Error precio")
    print(f'Nombre: {name}\nMarca: {brand}\nPrecio: {price}')   #Genera print con los datos extaidos
    sleep(1)
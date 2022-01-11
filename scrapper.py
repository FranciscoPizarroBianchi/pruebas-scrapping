from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from mysql_conn import conectar_bbdd,ejecutar_query,insertar_productos,insertar_precio_historico
from links import links_supermercados
import mysql.connector
from mysql.connector import Error
driver = webdriver.Firefox()     #Define el navegador a utilizar
driver.maximize_window()        #Maximizar ventana
from productos import Producto

def products_loop():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scrollear toda la pagina, para que termine de cargar
    driver.execute_script("window.scrollTo(0,0)") #Scrollear toda la pagina, para que termine de cargar
    sleep(0.2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scrollear toda la pagina, para que termine de cargar
    category_name = driver.find_element(By.CLASS_NAME,'title-with-bar-text').text
    products = driver.find_elements(By.CLASS_NAME,'shelf-item') #Buscar "tarjeta" de cada producto
    for product in products:
        type_sale=""
        original_price=""
        price=""
        url_img_content = product.find_element(By.CLASS_NAME,'shelf-product-image-island')
        url_product = url_img_content.find_element(By.TAG_NAME,'a').get_attribute('href')
        brand = product.find_element(By.CLASS_NAME,'shelf-product-brand').text
        name = product.find_element(By.CLASS_NAME,'shelf-product-title-text').text
        image = product.find_element(By.CLASS_NAME,'lazy-image').get_attribute('src')
        try:
            price = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'product-sigle-price-wrapper'))).text #Extrae el precio de producto, con la condicion de esperar max 3 segundos - Productos precio normal
        except TimeoutException or NoSuchElementException:
            try:
                price_content = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'promotion')))
                price = WebDriverWait(price_content,3).until(EC.presence_of_element_located((By.CLASS_NAME,'price-best'))).text #Extrae el precio de producto, con la condicion de esperar max 3 segundos - Productos bajados de precio
                type_sale = WebDriverWait(price_content,1).until(EC.presence_of_element_located((By.CLASS_NAME,'price-product-prom'))).text #Extrae el tipo de oferta (Promocion o descuento)
            except TimeoutException or NoSuchElementException:
                pass
        try:
            original_price = WebDriverWait(product,3).until(EC.presence_of_element_located((By.CLASS_NAME,'price-product-value'))).text
        except TimeoutException or NoSuchElementException:
            pass
            
        producto = Producto(name,price,image,url_product,brand,original_price,type_sale)
        producto.precio_originalNULL()
        producto.tipo_promocionNULL()
        print(producto)
        
        conexion = conectar_bbdd()
        ejecutar_query(conexion,insertar_productos(producto))
        ejecutar_query(conexion,insertar_precio_historico(producto))


for i in range(0,len(links_supermercados)):
    for j in range(0,len(links_supermercados[i])):
        driver.get(links_supermercados[i][j])
        wait = WebDriverWait(driver, 10)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scrollear toda la pagina, para que termine de cargar
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'shelf-item')))


        super_category_name = driver.find_element(By.CLASS_NAME,'title-with-bar-text').text


        super_category = driver.find_element(By.CLASS_NAME,'category-aside-list')
        super_subcategorys = super_category.find_elements(By.CLASS_NAME,'catalog-aside-nav-item')
        super_subcategory_href = [super_subcategory.find_element(By.TAG_NAME,'a').get_attribute('href') for super_subcategory in super_subcategorys]
        for url in super_subcategory_href:
            driver.get(url)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'shelf-list')))


            category = driver.find_element(By.CLASS_NAME,'category-aside-list') #Variable que almacena el elemento que contiene a las categorias
            subcategorys = category.find_elements(By.CLASS_NAME,'catalog-aside-nav-item') #Variable que accede a cada categoria
            subcategory_href = [subcategory.find_element(By.TAG_NAME,'a').get_attribute('href') for subcategory in subcategorys] #Extrae los href de cada categoria
            for url in subcategory_href: #Por cada href que haya encontrado, comenzará bucle
                driver.get(url) #redirecciona a cada categoria
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'shelf-list')))



                pages = driver.find_elements(By.CLASS_NAME,'page-number')   #Variable que accede a cada numero de pagina
                subcategory_url = [page.get_attribute("innerHTML") for page in pages]   #Extrae todos los textos de los numeros de pagina
                if(len(subcategory_url)!=0):
                    for url_subcategory in subcategory_url: 
                        print(url_subcategory)
                        driver.get(url+'?page={}'.format(url_subcategory)) #Redirecciona a cada pagina que exista en determinada categoria
                        wait = WebDriverWait(driver, 10)
                        driver.execute_script("window.scrollTo(0, 0);")
                        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'shelf-list')))
                        products_loop()
                else:
                    products_loop()


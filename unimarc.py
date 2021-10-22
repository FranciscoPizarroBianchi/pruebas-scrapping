from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link='https://www.unimarc.cl/desayuno-y-dulces/cereales'    #Enlace a la pagina scrappear
driver = webdriver.Firefox()
driver.maximize_window()        #For maximizing window
driver.implicitly_wait(20)      #Espera como maximo 20 segundos para que cargue la pagina
driver.get(link)               #
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


#Productos
#products = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'unimarc-pixels-search-0-x-galleryItem unimarc-pixels-search-0-x-galleryItem--normal pa4')))
sleep(5)
wait = WebDriverWait(driver, 100)

wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'product-item')))

products = driver.find_elements(By.CLASS_NAME,'product-item')
for product in products:
    name = product.find_element(By.CLASS_NAME,'product-title').text
    brand = product.find_element(By.CLASS_NAME,'brand-name').text
    try:
        price = product.find_element(By.CLASS_NAME,'product-price').text
    except NoSuchElementException:
        try:
            price = product.find_element(By.CLASS_NAME,'product-price-normal').text
        except:
            print("Error precio")
    print(f'Nombre: {name}\nMarca: {brand}\nPrecio: {price}')
    sleep(1.5)
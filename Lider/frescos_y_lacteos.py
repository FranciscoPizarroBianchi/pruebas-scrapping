from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException

driver = webdriver.Firefox()     #Define el navegador a utilizar
driver.maximize_window()        #Maximizar ventana

driver.get('https://www.lider.cl/supermercado/category/Frescos-y-Lácteos')
wait = WebDriverWait(driver, 10)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scrollear toda la pagina, para que termine de cargar
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'box-product')))

products = driver.find_elements(By.CLASS_NAME,'box-product')

for product in products:
    name =  product.find_element(By.CLASS_NAME,'product-description').text
    brand = product.find_element(By.CLASS_NAME,'product-name').text
    print(brand,name)
    x = product.find_element(By.CLASS_NAME('product-addtocart -no-visible'))
    available = x.is_displayed()
    print(available)
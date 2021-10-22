import random as rd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Rotar proxy
# cmd = 'python proxyrotate.py'

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
link = 'https://www.jumbo.cl/lacteos-y-bebidas-vegetales'
driver = webdriver.Firefox()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
driver.get(link)

button = driver.find_element(By.CLASS_NAME,'page-number')
#for npage in npages:
#     npagina = npage.text
#     print(npagina)
#     sleep(0.2)

products = driver.find_elements(By.CLASS_NAME,'shelf-item')
#for product in products:
#     nombre = product.find_element(By.CLASS_NAME,'shelf-product-title-text').text
#     print(nombre)
#     sleep(1)

while True:
     try:
          for product in products:
               nombre = product.find_element(By.CLASS_NAME,'shelf-product-title-text').text
               print(nombre)
               sleep(1)
          button.click()
          driver.implicitly_wait(10)
     except (TimeoutException, WebDriverException) as e:
        print("Ultima pagina alcanzada")
        break

driver.quit()
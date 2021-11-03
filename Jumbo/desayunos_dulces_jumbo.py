from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException

driver = webdriver.Safari()     #Define el navegador a utilizar
driver.maximize_window()        #Maximizar ventana

driver.get('https://www.jumbo.cl/desayuno-y-dulces/desayuno?page=1')
sleep(5)
slides = driver.find_element(By.CLASS_NAME,'slides')
pages = slides.find_elements(By.CLASS_NAME,'page-number')
for e in pages:
    print(e.text)
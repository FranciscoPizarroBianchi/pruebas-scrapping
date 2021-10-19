from bs4 import BeautifulSoup
import requests
import subprocess
from selenium import webdriver

#Rotar proxy
# cmd = 'python proxyrotate.py'

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
link = 'https://www.jumbo.cl/lacteos-y-bebidas-vegetales'


driver = webdriver.Firefox()
driver.get(link)

soup = BeautifulSoup(driver.page_source,'html.parser')


listaProductos = soup.find_all('li', class_='shelf-item')
print(listaProductos)
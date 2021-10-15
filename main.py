from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.linio.cl/cm/venta-gamer?skus=ON913EL07QN1ULACL&utm_source=SIS_LI_HoldingBanner-1.1&utm_medium=referral&utm_campaign=Tecnologia-Gamer').text
soup = BeautifulSoup(html_text,'lxml')
products = soup.find_all('div', class_='catalogue-product row')
with open(f'posts/productos.txt','w',encoding='utf-8') as f:
    for index, product in enumerate(products):
        tittle = product.find('img')['alt'].replace(' ','')
        price = product.find('span', class_='price-main-md').text.replace(' ','')
        f.write(f"Nombre producto: {tittle}")
        f.write(f"Precio: {price}")
        print(f'Archivo guardado: {index}')

import requests
from bs4 import BeautifulSoup
from flaskr.db import get_db

def ScrappingPani():
    url = "https://eltornillo.com.mx/tienda-en-linea/tornillos.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    productos = soup.find_all('div', class_='product details product-item-details')

    # Conexión a la base de datos
    db = get_db()

    # Recorre cada producto y extrae la información deseada
    for producto in productos:
        nombre = producto.find('a', class_='product-item-link').text.strip()
        link = producto.find('a', class_='product-item-link')['href']  # Extraer el link del producto
        precio_texto = producto.find('span', class_='price').text.strip().replace('$', '').replace(',', '')
        try:
            precio = float(precio_texto)
        except ValueError:
            precio = 0.0  # Manejar el caso si el precio no se puede convertir

        # Insertar en la tabla 'Tornillos' incluyendo el link
        db.execute(
            "INSERT INTO Tornillos (Producto, Precio, Vinculo) VALUES (?, ?, ?)",
            (nombre, precio, link)
        )
       
    db.commit()



def ScrappingSebas():
    url = 'https://www.todocuadros.com.mx/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtener los títulos, precios y enlaces de los productos
    products = soup.find_all('product-card', class_='product-card')

    db = get_db()

    for product in products:
        # Título
        title_tag = product.find('a', class_='product-title h6')
        titulo = title_tag.text.strip() if title_tag else "Sin título"

        # Precio
        price_tag = product.find('sale-price', class_='h6 text-subdued')
        precio = price_tag.text.strip() if price_tag else "Sin precio"

        # Enlace
        link_tag = product.find('a', class_='product-card__media')
        enlace = "https://www.todocuadros.com.mx" + link_tag['href'] if link_tag else "Sin enlace"

        # Insertar en la tabla 'Arte'
        db.execute(
            "INSERT INTO Arte (Titulo, Precio, Vinculo) VALUES (?, ?, ?)",
            (titulo, precio, enlace)
        )
    db.commit()

def ScrappingLuis():
    url = 'https://coleccionsergiobustamante.com.mx/en/collections/esculturas'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('p', class_='product__grid__title')
    prices = soup.find_all('span', class_='money')

    db = get_db()

    for title, price in zip(titles, prices):
        price_text = price.text.strip()
        if price_text != "$0.00":
            nombre = title.text.strip()

            # Insertar en la tabla 'Esculturas'
            db.execute(
                "INSERT INTO Esculturas (Producto, Precio) VALUES (?, ?)",
                (nombre, price_text)
            )
    db.commit()
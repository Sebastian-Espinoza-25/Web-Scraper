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
        precio_texto = producto.find('span', class_='price').text.strip().replace('$', '').replace(',', '')
        try:
            precio = float(precio_texto)
        except ValueError:
            precio = 0.0  # Manejar el caso si el precio no se puede convertir

        # Insertar en la tabla 'Tornillos'
        db.execute(
            "INSERT INTO Tornillos (Producto, Precio) VALUES (?, ?)",
            (nombre, precio)
        )
    db.commit()


def ScrappingSebas():
    url = 'https://www.todocuadros.com.mx/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('a', class_='product-title')
    prices = soup.find_all('sale-price', class_='h6 text-subdued')

    db = get_db()

    for title, price in zip(titles, prices):
        titulo = title.text.strip()
        precio = price.text.strip()

        # Insertar en la tabla 'Arte'
        db.execute(
            "INSERT INTO Arte (Titulo, Precio) VALUES (?, ?)",
            (titulo, precio)
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

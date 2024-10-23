from flask import (
    Blueprint, g, render_template
)
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()

    if g.user:  # Si el usuario ha iniciado sesión
        user_id = g.user['id']
        selections = db.execute(
            'SELECT content_type FROM user_content_selection WHERE user_id = ?', (user_id,)
        ).fetchall()

        selected_content = [s['content_type'] for s in selections]

        tornillos, arte, esculturas = [], [], []

        # Mostrar solo el contenido seleccionado por el usuario
        if 'Tornillos' in selected_content:
            tornillos = db.execute('SELECT Producto, Precio FROM Tornillos').fetchall()

        if 'Arte' in selected_content:
            arte = db.execute('SELECT Titulo, Precio FROM Arte').fetchall()

        if 'Esculturas' in selected_content:
            esculturas = db.execute('SELECT Producto, Precio FROM Esculturas').fetchall()

        print("Contenido seleccionado: ", selected_content)
        print("Datos de Arte: ", arte)

        return render_template('blog/index.html', tornillos=tornillos, arte=arte, esculturas=esculturas)

    else:  # Si el usuario NO ha iniciado sesión, mostrar todos los datos
        tornillos = db.execute('SELECT Producto, Precio FROM Tornillos').fetchall()
        arte = db.execute('SELECT Titulo, Precio FROM Arte').fetchall()
        esculturas = db.execute('SELECT Producto, Precio FROM Esculturas').fetchall()

        return render_template('blog/index.html', tornillos=tornillos, arte=arte, esculturas=esculturas)

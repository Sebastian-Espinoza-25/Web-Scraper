import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('scrape-data')
def scrape_data_command():
    """Scrapes data from three websites and saves to the database."""
    # Importar scrapers dentro de la función
    from flaskr.scrapers import ScrappingPani, ScrappingSebas, ScrappingLuis

    click.echo('Starting scraping process...')
    
    ScrappingPani()
    click.echo('Scrapped Tornillos data.')
    
    ScrappingSebas()
    click.echo('Scrapped Arte data.')
    
    ScrappingLuis()
    click.echo('Scrapped Esculturas data.')

    click.echo('Scraping process completed and data stored in the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(scrape_data_command)

import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'flask_db' not in g:
        g.flask_db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.flask_db.row_factory = sqlite3.Row
    return g.flask_db

def close_flask_db(e=None):
    flask_db = g.pop('flask_db', None)

    if flask_db is not None:
        flask_db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
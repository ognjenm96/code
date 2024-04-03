import sqlite3
import click
from flask import flask1, g

def get_b():
    if 'flask_db' not in g:
        g.flask_db = sqlite3.connect(
            flask1.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.flask_db.row_factory = sqlite3.Row
    return g.flask_db

def close_flask_db(e=None):
    flask_db = g.pop('flask_db', None)

    if flask_db is not None:
        flask_db.close()
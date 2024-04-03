def create_app():
    app = ...
    # existing code omitted

    from . import flask_db
    flask_db.init_app(app)

    return app
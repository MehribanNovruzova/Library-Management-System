# helpers/db.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
db = SQLAlchemy()

class DatabaseHelper:
    def __init__(self, app):
        self.app = app
        db.init_app(app)

    def create_tables(self):
        with self.app.app_context():
            db.create_all()

    def execute_query(self, query, params=None):
        with self.app.app_context():
            result = db.session.execute(query, params or {})
            db.session.commit()
            return result

    def fetch_all(self, query, params=None):
        with self.app.app_context():
            result = db.session.execute(query, params or {})
            return result.fetchall()

    def fetch_one(self, query, params=None):
        with self.app.app_context():
            result = db.session.execute(query, params or {})
            return result.fetchone()

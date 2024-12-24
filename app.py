# app.py

from flask import Flask, jsonify, request
from models import Book, Member, Loan
from helpers.db import DatabaseHelper

app = Flask(__name__)

# Configure your database URI (using SQLite for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the DatabaseHelper
db_helper = DatabaseHelper(app)

# Create tables
db_helper.create_tables()

# In-memory storage for simplicity (you can remove this if using a database)
books = {}
members = {}
loans = {}
book_id_counter = 1
member_id_counter = 1
loan_id_counter = 1

# Your existing routes go here...

if __name__ == '__main__':
    app.run(debug=True)

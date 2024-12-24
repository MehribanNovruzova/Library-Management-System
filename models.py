from helpers.db import db

class Book(db.Model):
    __tablename__ = 'books'
    
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)

    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

class Member(db.Model):
    __tablename__ = 'members'
    
    member_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Member {self.name}>"

class Loan(db.Model):
    __tablename__ = 'loans'
    
    loan_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'), nullable=False)

    book = db.relationship('Book', backref='loans')
    member = db.relationship('Member', backref='loans')

    def __init__(self, book_id, member_id):
        self.book_id = book_id
        self.member_id = member_id

    def __repr__(self):
        return f"<Loan {self.loan_id} for Book ID {self.book_id} by Member ID {self.member_id}>"

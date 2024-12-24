class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Loan:
    def __init__(self, loan_id, book_id, member_id):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id

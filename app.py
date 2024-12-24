from flask import Flask, jsonify, request
from models import Book, Member, Loan

app = Flask(__name__)

# In-memory storage for simplicity
books = {}
members = {}
loans = {}
book_id_counter = 1
member_id_counter = 1
loan_id_counter = 1

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.json
    book = Book(book_id_counter, data['title'], data['author'], data['available_copies'])
    books[book_id_counter] = book
    book_id_counter += 1
    return jsonify({"message": "Book added successfully!"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([{"book_id": book.book_id, "title": book.title, "author": book.author, "available_copies": book.available_copies} for book in books.values()])

@app.route('/members', methods=['POST'])
def add_member():
    global member_id_counter
    data = request.json
    member = Member(member_id_counter, data['name'])
    members[member_id_counter] = member
    member_id_counter += 1
    return jsonify({"message": "Member added successfully!"}), 201

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify([{"member_id": member.member_id, "name": member.name} for member in members.values()])

@app.route('/loans', methods=['POST'])
def create_loan():
    global loan_id_counter
    data = request.json
    if data['book_id'] in books and books[data['book_id']].available_copies > 0:
        loan = Loan(loan_id_counter, data['book_id'], data['member_id'])
        loans[loan_id_counter] = loan
        books[data['book_id']].available_copies -= 1  # Decrease available copies
        loan_id_counter += 1
        return jsonify({"message": "Loan created successfully!"}), 201
    else:
        return jsonify({"message": "Book not available!"}), 400

@app.route('/loans', methods=['GET'])
def get_loans():
    return jsonify([{"loan_id": loan.loan_id, "book_id": loan.book_id, "member_id": loan.member_id} for loan in loans.values()])

@app.route('/return', methods=['POST'])
def return_loan():
    data = request.json
    loan_id = data['loan_id']
    if loan_id in loans:
        book_id = loans[loan_id].book_id
        books[book_id].available_copies += 1  # Increase available copies
        del loans[loan_id]  # Remove the loan
        return jsonify({"message": "Book returned successfully!"}), 200
    else:
        return jsonify({"message": "Loan not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)

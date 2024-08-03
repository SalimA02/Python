from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for the API
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# GET /books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# GET /books/<id>
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if book:
        return jsonify({"book": book[0]})
    else:
        return jsonify({"message": "Book not found"})

# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json['title'],
        "author": request.json['author']
    }
    books.append(new_book)
    return jsonify({"message": "Book added successfully"})

# PUT /books/<id>
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if book:
        book[0]['title'] = request.json.get('title', book[0]['title'])
        book[0]['author'] = request.json.get('author', book[0]['author'])
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"message": "Book not found"})

# DELETE /books/<id>
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if book:
        books.remove(book[0])
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"message": "Book not found"})

if __name__ == '__main__':
    app.run(debug=True)
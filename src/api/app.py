
from flask import Flask, request, jsonify

from src.book import Book
from src.library import Library, validate_isbn


def create_app():
    app = Flask(__name__)

    # Create one Library instance for this application.
    library = Library()

    @app.route("/members", methods=["POST"])
    def add_member():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "JSON object required."}), 400

        member_id = data.get("id")

        if not isinstance(member_id, (str, int)) or isinstance(member_id, bool):
            return jsonify({"error": "Valid member ID is required."}), 400

        member_id = str(member_id)

        if not member_id.strip():
            return jsonify({"error": "Member ID cannot be empty."}), 400

        try:
            library.register_member(member_id)
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

        return jsonify({"id": member_id}), 201

    @app.route("/books", methods=["POST"])
    def add_book():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "JSON object required."}), 400

        required_fields = ["title", "isbn", "author", "total_copies"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        title = data["title"]
        isbn = data["isbn"]
        author = data["author"]
        copies = data["total_copies"]

        if not all(isinstance(value, str) and value.strip()
                   for value in [title, isbn, author]):
            return jsonify({"error": "Title, ISBN and author must be non-empty strings."}), 400

        if not validate_isbn(isbn):
            return jsonify({"error": "ISBN must contain exactly 13 digits."}), 400

        if not isinstance(copies, int) or isinstance(copies, bool) or copies < 0:
            return jsonify({"error": "total_copies must be a non-negative integer."}), 400

        try:
            book = Book(title, author, isbn, copies)
            library.add_book(book)
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

        return jsonify({
            "title": book.title,
            "isbn": book.book_id,
            "author": book.author,
            "available_copies": book.copies
        }), 201

    @app.route("/books", methods=["GET"])
    def get_books():
        books = []

        for book in library.books.values():
            books.append({
                "title": book.title,
                "isbn": book.book_id,
                "author": book.author,
                "available_copies": book.copies
            })

        return jsonify(books), 200

    @app.route("/books/<isbn>", methods=["GET"])
    def get_book(isbn):
        book = library.books.get(isbn)

        if book is None:
            return jsonify({"error": "Book not found."}), 404

        return jsonify({
            "title": book.title,
            "isbn": book.book_id,
            "author": book.author,
            "available_copies": book.copies
        }), 200

    @app.route("/members/<member_id>/borrow", methods=["POST"])
    def borrow_book(member_id):
        if member_id not in library.members:
            return jsonify({"error": "Member not found."}), 404

        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "JSON object required."}), 400

        isbn = data.get("isbn")

        if not isinstance(isbn, str) or not isbn.strip():
            return jsonify({"error": "Valid ISBN is required."}), 400

        try:
            library.borrow_book(member_id, isbn)
        except ValueError as error:
            message = str(error)
            status = 404 if message == "Book not found." else 400
            return jsonify({"error": message}), status

        return jsonify({
            "isbn": isbn,
            "available_copies": library.books[isbn].copies
        }), 200

    @app.route("/members/<member_id>/return", methods=["POST"])
    def return_book(member_id):
        if member_id not in library.members:
            return jsonify({"error": "Member not found."}), 404

        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "JSON object required."}), 400

        isbn = data.get("isbn")

        if not isinstance(isbn, str) or not isbn.strip():
            return jsonify({"error": "Valid ISBN is required."}), 400

        days_overdue = data.get("days_overdue", 0)

        try:
            library.return_book(member_id, isbn, days_overdue)
        except ValueError as error:
            message = str(error)
            status = 404 if message in ("Member not found.", "Book not found.") else 400
            return jsonify({"error": message}), status

        return jsonify({
            "isbn": isbn,
            "available_copies": library.books[isbn].copies,
            "days_overdue": days_overdue
        }), 200

    @app.route("/members/<member_id>/fines", methods=["GET"])
    def get_fines(member_id):
        try:
            result = library.get_member_fines(member_id)
        except ValueError as error:
            return jsonify({"error": str(error)}), 404

        return jsonify(result), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

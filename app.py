from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
'''WSGI'''

###WSGI Application cd 
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'author', 'price']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        new_book = Book(
            title=data['title'],
            author=data['author'],
            price=float(data['price'])
        )
        
        db.session.add(new_book)
        db.session.commit()
        
        return jsonify({'message': 'Book added successfully', 'book': new_book.to_dict()}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        return jsonify({'books': [book.to_dict() for book in books]}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    try:
        book = Book.query.get(id)
        if book:
            return jsonify({'book': book.to_dict()}), 200
        return jsonify({'message': 'Book not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    try:
        book = Book.query.get(id)
        if not book:
            return jsonify({'message': 'Book not found'}), 404
        
        data = request.get_json()
        
        if 'title' in data:
            book.title = data['title']
        if 'author' in data:
            book.author = data['author']
        if 'price' in data:
            book.price = float(data['price'])
        
        db.session.commit()
        return jsonify({'message': 'Book updated successfully', 'book': book.to_dict()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        book = Book.query.get(id)
        if not book:
            return jsonify({'message': 'Book not found'}), 404
        
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Search endpoint
@app.route('/books/search', methods=['GET'])
def search_books():
    try:
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        
        query = Book.query
        
        if title:
            query = query.filter(Book.title.ilike(f'%{title}%'))
        if author:
            query = query.filter(Book.author.ilike(f'%{author}%'))
        
        books = query.all()
        return jsonify({'books': [book.to_dict() for book in books]}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


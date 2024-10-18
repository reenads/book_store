from lib.book import *

class BookRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books
    
    def find(self, book_id):
        rows = self._connection.execute('SELECT * FROM books WHERE id = %s', [book_id])
        row = rows [0]
        return Book(row["id"], row["title"], row["author_name"])

    def create(self, book):
        self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [book.title, book.author_name])
        return None
    
    def delete(self, book_id):
        self._connection.execute('DELETE FROM books WHERE id = %s', [book_id])
        return None
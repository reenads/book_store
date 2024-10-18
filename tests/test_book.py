from lib.book import *

"""
Book constructs with an id, title and author name
"""
def test_if_Book_is_created():
    book = Book(1, "White Teeth", "Zadie Smith")
    assert book.id == 1
    assert book.title == "White Teeth"
    assert book.author_name == "Zadie Smith"

"""
We can format the list of books nicely

"""

def test_books_format_nicely():
    book = Book(1, "White Teeth", "Zadie Smith")
    assert str(book) == "Book(1, White Teeth, Zadie Smith)"

"""
We can compare two identical artists
And have them be equal
"""

def test_the_same_book_object_is_equal():
    book_1 = Book(1, "White Teeth", "Zadie Smith")
    book_2 = Book(1, "White Teeth", "Zadie Smith")
    assert book_1 == book_2
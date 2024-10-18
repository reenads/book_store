from lib.book_repository import *
from lib.book import *
"""
When we call all method on BookRepository
We get a list of all the Book objects reflecting the seed data.
"""
def test_all(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    books = repository.all()
    assert books == [Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
Book(3, 'Emma', 'Jane Austen'),
Book(4, 'Dracula', 'Bram Stoker'),
Book(5, 'The Age of Innocence', 'Edith Wharton')]

"""
When we call the find method on BookRepository
We get a single Book object reflecting the seed data.
"""
def test_find_one_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    books = repository.find(2)
    assert books == Book(2, 'Mrs Dalloway', 'Virginia Woolf')


"""
When we call the create method on BookRepository
We get a new record in the books database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    repository.create(Book(None, "White Teeth", "Zadie Smith"))
    result = repository.all()
    assert result == [Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
Book(3, 'Emma', 'Jane Austen'),
Book(4, 'Dracula', 'Bram Stoker'),
Book(5, 'The Age of Innocence', 'Edith Wharton'),
Book(6, "White Teeth", "Zadie Smith")]

"""
# When we call delete on the BookRepository 
# We remove a record from the database associated with the id.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    books = repository.delete(2)
    result = repository.all()
    assert result == [Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
Book(3, 'Emma', 'Jane Austen'),
Book(4, 'Dracula', 'Bram Stoker'),
Book(5, 'The Age of Innocence', 'Edith Wharton')]

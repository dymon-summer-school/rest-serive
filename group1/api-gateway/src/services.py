
from repository import Fake_DB


# get books
def get_books() -> list:
    """-"""
    books: list = Fake_DB.get_books()
    return books


# get book by id
def get_book_by_id(id: int | str) -> dict:
    """-"""
    id = int(id)
    book: dict = Fake_DB.get_book_by_id(id)
    return book


# add book
def add_book(book: dict) -> int:
    """-"""
    # add book to FAKE_DB
    book_id: int = Fake_DB.add_book(book) 
    return book_id


# get bundesland by name
def get_bundesland_by_name(name: str) -> dict:
    """-"""
    bundesland: dict = Fake_DB.get_bundesland_by_name(name)
    return bundesland

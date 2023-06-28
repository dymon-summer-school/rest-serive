
import json

import geopandas as gpd
import pandas as pd

df_books: pd.DataFrame = pd.read_csv('data/books.csv')
gdf = gpd.read_file("data/oesterreich.json", driver='GeoJSON')


class Fake_DB():

    @staticmethod
    def get_books() -> list:
        """Returns all books as an array with the books in dict(json) format"""
        return df_books.to_dict('records')

    @staticmethod
    def get_book_by_id(book_id: int) -> dict:
        """Returns one book with that id as an dict(json)"""
        df_book: pd.DataFrame = df_books[df_books["id"] == book_id]

        # if a book was found, strip index and return the book as a dict
        if len(df_book) > 0:
            return df_book.to_dict("records")[0]
        return {}

    @staticmethod
    def add_book(book: dict) -> int:
        global df_books
        # get last id and add 1
        new_id: int = int(df_books.iloc[-1]["id"]+1)  # cast to int, otherwise np.int64
        book["id"] = new_id
        df_books = pd.concat([df_books, pd.DataFrame([book.values()], columns=list(book.keys()))], ignore_index=True)
        return new_id

    @staticmethod
    def get_bundesland_by_name(name: str) -> dict:
        """Returns an area with that name as an dict(json)"""
        df_bundesland = gdf[gdf["name"] == name]

        # if a book was found, strip index and return the book as a dict
        if len(df_bundesland) > 0:
            return json.loads(df_bundesland.to_json())  # type: ignore
        return {}

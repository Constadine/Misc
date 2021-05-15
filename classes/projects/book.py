class Book:
    def __init__(self, title, authors, price, copies) -> None:
        self.title = title
        self.authors = authors
        self.price = price
        self.copies = copies

    def print_full_title(self):
        authors_names = [author.fullname for author in self.authors]
        print(f"'{self.title}' by " + ", ".join(authors_names))

    def add_author(self, author):
        self.authors.append(author)


class Author:
    def __init__(self, fullname, email) -> None:
        self.fullname = fullname
        self.email = email


author1 = Author("Bob Patterson", "bob@pcookbook.com")
author2 = Author("James McConan", "james@pcookbook.com")


book = Book("The Ultimate Python Cookbook", [
            author1, author2], 18.25, 43)

book.print_full_title()
book.add_author(Author("Tom Rossbow", "tom@pcookbook.com"))
book.print_full_title()

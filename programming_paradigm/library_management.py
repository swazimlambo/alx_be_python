class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:    
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self.add_book.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return True
        print(f"Book '{title} not available")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print("Book not available")

    def list_available_books(self):
        available_books = [book for  book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book) 

        


        
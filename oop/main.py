import math
from book_class import Book
from library_system import Book, EBook, PrintBook, Library 
from  polymorphism_demo import Shape, Rectangle, Circle
from class_static_methods_demo import Calculator

def main():
    #Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    #Demonstrating the __str__ method
    print(my_book)

    #Demonstrating the __repr__ method
    print(repr(my_book))

    #Deleting a book instance to trigger __del__
    del my_book


def main():
    #Create a library instance
    my_library = Library()

    #Create instance of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stepheson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    #Add books to the Library
    my_library.add_book(classic_book)    
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    #List all books in the library
    my_library.list_books()
    

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]    

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


def main():
    #Using the static method
    sum_result = Calculator.add(10, 5)       
    print(f"The sum is: {sum_result}")

    #Using the class method
    product_result = Calculator.multiply(10,5)
    print(f"The product is: {product_result}")

if __name__== "__main__":
    main()    
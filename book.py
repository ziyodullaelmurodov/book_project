class Book:
    def __init__(self, title: str, author: str, genre: str, publication_year: int, price: float, availability: bool=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.__price = price
        self.availability = availability

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def apply_discount(self, discount_percentage):
        self.__price = discount_percentage

# Create an instance of the Book class
book = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, 10.99, True)
# Get the price of the book
price = book.get_price()
print(price)
book.apply_discount(price-(price * 0.10))
price = book.get_price()
print(price)

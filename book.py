class Book:
    #Constructor Blueprint for title, author, and isbn
    def __init__(self, title, author, isbn = "N/A"):
        # Initialize a new book instance
        self.title = title 
        self.author = author 
        self.isbn = isbn
        
    # __str__ gives a friendly string when printing 
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}" 
    
    
    def get_details(self):
            return {
        "title": self.title,
        "author": self.author,
        "isbn": self.isbn
    } 
    
#Create an Instances (real books)
my_favorite_book = Book("The way of kings", "Brandon Sanderson", "9780765326355" )
classic_book = Book("1984", "George Orwell","9780451524935")

# Print the objects (calls __str__)
print(my_favorite_book)    # Output: Book Title: The way of kings, Book Author: Brandon Sanderson
print(classic_book)        # Output: Book Title: 1984, Book Author: George Orwell


#Print full details using get_details method
print(my_favorite_book.get_details())
print(classic_book.get_details()) 

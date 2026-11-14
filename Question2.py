class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(self.title, "-", self.author)

b1 = Book("Python", "Ali")
b2 = Book("IoT", "Sara")
b3 = Book("AI", "Ahmed")
b1.display_info()
b2.display_info()
b3.display_info()

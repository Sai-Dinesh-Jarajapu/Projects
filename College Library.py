class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book +"* " )
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
    
    def returnBook(self, bookName):
        if bookName not in self.books:
            self.books.append(bookName)
            print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        else:
            print("This book is already available in the library. Please check if you returned the correct book.")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBookName(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
student = Student()
welcomeMsg = '''\n ====== Welcome to Central Library ======
    Please choose an option:
    1. List all the books
    2. Request a book
    3. Return a book
    4. Exit the Library
    '''
print(welcomeMsg)
while(True):
    a = int(input("Enter a choice: "))
    if a == 1:
        centraLibrary.displayAvailableBooks()
    elif a == 2:
        centraLibrary.borrowBook(student.requestBook())
    elif a == 3:
        centraLibrary.returnBook(student.returnBookName())
    elif a == 4:
        print("Thanks for choosing Central Library. Have a great day ahead!")
        break
    else:
        print("Invalid Choice!")
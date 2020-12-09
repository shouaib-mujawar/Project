# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from BookItem import BookItem

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):

    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued={}
        self.different_book_count=Catalog.different_book_count
        self.books=Catalog.books
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,isbn,days=10):
        book=Catalog.searchByName(name)
        if book:
            bookitem=book.searchBookItem(isbn)
            book.removeBookItem(bookitem)
            print(book,"Book issued for",days,"days to",self.name)
            self.issued[book]=(days)
        else:
            print("The book you asking for is not in the library at this very moment")

    #assume name is unique
    def returnBook(self,name,isbn,rack,days):
        book=Catalog.searchByName(name)
        if book:
            Catalog.addBookItem(self,book,isbn,rack)
            if (self.issued.get(book))<days:
                print(self.name,"You have to pay the fine")
            else:
                print("Thanks for returning book on time")
        else:
            print("Book Doesn't exist ask Librarian to add book")
            
class Librarian(User):

    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        Catalog.__init__(self)

    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages):
        return Catalog.addBook(self,name,author,publish_date,pages)
    
    def addBookItem(self,book,isbn,rack):
        Catalog.addBookItem(self,book,isbn,rack)

    def removeBookItem(self,name,isbn):
        Catalog.removeBookItem(self,name,isbn)
    
    def removeBookFromCatalog(self,name):
        Catalog.removeBookFromCatalog(self,name)

    def displayAllBooks(self):
        return Catalog.displayAllBooks(self)
    

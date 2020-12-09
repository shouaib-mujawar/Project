# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    different_book_count = 0
    books = []

    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        Catalog.different_book_count += 1
        Catalog.books.append(b)
        return b
    
    #Only available to admin
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
   
    @classmethod    
    def searchByName(cls,name):
        for book in Catalog.books:
            if name.strip() == book.name:
                return book
    @classmethod
    def searchByAuthor(cls,author):
        for book in Catalog.books:
            if author.strip() == book.author:
                return book
        
        
    def displayAllBooks(self):
        print ('Different Book Count',Catalog.different_book_count)
        c = 0
        for book in Catalog.books:
            c += book.total_count
            book.printBook()
        
        print ('Total Book Count',c)
        
    def removeBookItem(self,name,isbn):
        book = Catalog.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)

    def removeBookFromCatalog(self,name):
        for value in Catalog.books:
            if name.strip()==value.name:
                Catalog.books.remove(value)
                Catalog.different_book_count -= 1
                print(value,"book removed from Catalog")

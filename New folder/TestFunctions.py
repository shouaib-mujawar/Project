# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 

b=librarian.addBook('Moonwalking with Einstien','J Foer', '2017',318)
librarian.addBookItem(b, '117hg','H1B2')
librarian.addBookItem(b, '118hg','H1B2')
librarian.addBookItem(b, '119hg','H1B2')
librarian.addBookItem(b, '120hg','H1B2')
librarian.addBookItem(b, '121hg','H1B2')
b=librarian.addBook('Shoe Dog','Phil Knight', '2015',312)
librarian.addBookItem(b, '123hg','H1B2')
librarian.addBookItem(b, '124hg','H1B4')
librarian.addBookItem(b, '125hg','H1B5')
b=librarian.addBook('In Search of Lost Time','Marcel Proust', '1913',400)
librarian.addBookItem(b, '143hg','H1B7')
librarian.addBookItem(b, '144hg','H1B6')
librarian.addBookItem(b, '145hg','H1B7')
b=librarian.addBook('One Hundred Years of Solitude','Gabriel Garcia Marquez', '2009',350)
librarian.addBookItem(b, '153hg','H1B8')
librarian.addBookItem(b, '154hg','H1B8')
librarian.addBookItem(b, '155hg','H1B9')
b=librarian.addBook('The Great Gatsby','F. Scott Fitzgerald', '1922',602)
librarian.addBookItem(b, '223hg','H1B1')

librarian.displayAllBooks()


# Member Methods

m=Member("Vish","Bangalore",23,'asljlkj22','std1233')
m.issueBook("Shoe Dog",'123hg',15)
m.issueBook("One Hundred Years of Solitude",'153hg',12)

m1=Member("Tom","Bangalore",23,'asljlkj21','std1234')
m1.issueBook("Moonwalking with Einstien","119hg")

librarian.displayAllBooks()



librarian.removeBookFromCatalog("The Great Gatsby")
librarian.removeBookItem("In Search of Lost Time","143hg")

librarian.displayAllBooks()



m.returnBook("Shoe Dog","123hg","H1B2",10)
m1.returnBook("Moonwalking with Einstien","124hg","H1B2",11)

librarian.displayAllBooks()
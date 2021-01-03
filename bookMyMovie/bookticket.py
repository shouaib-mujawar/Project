import mysql.connector
cn=mysql.connector.connect(user="root",password="qwerty",host="localhost",database="bookticket")
mycursor=cn.cursor()

class Interaction:
    def __init__(self):
        print("Welcome to the theater")
        self.row=int(input("Enter no of rows:"))
        self.column=int(input("Enter no of seats in each row:"))
        print("1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show Booked Tickets User Info \n0. Exit")
        self.option=int(input())
        self.details=[]
        self.bookseat=[]
        self.half=[]
        self.user_deets={}    
        
        while True:
            if self.option==1:
                print("Cinema:")
                for val in range(1,self.column+1):
                    print('',val,end="")
                print()
                mycursor.execute('select s_row,s_col from bookedby;')
                bookedseat=mycursor.fetchall()
                for i in range(1,self.row+1): 
                    print(i,end=" ")
                    for j in range(1,self.column+1):
                        if (i,j) in bookedseat:
                            print('B',end=' ')
                        else:
                            print("S",end=" ")
                    print()
                print("1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show Booked Tickets User Info \n0. Exit")
                self.option=int(input())
         
            elif self.option==2:
                self.bookseat=input("Enter the row and column by using comma:").split(',')
                for val in self.bookseat:
                    self.details.append(val)
                val=self.bookseat[0]
                val2=self.bookseat[1]
                if int(val2)<=self.column and int(val)<=self.row:
                    if self.row*self.column>60:
                        self.firsthalf=self.row//2
                        for fh in range(1,self.firsthalf+1):
                            self.half.append(fh)
                        if int(val) in self.half:
                            self.ticket_price=10
                        else:
                            self.ticket_price=8
                    else:
                        self.ticket_price=10        
                else:
                    print("row or column out of range")
                    break
                
                print("The ticket price is",self.ticket_price,"$")
                self.ticket=(input("\nDo you want to book??(Y/N)")).lower()
                if self.ticket=="y":
                    self.name=input("Enter your name:")
                    self.details.append(self.name)
                    self.gender=input("Enter your gender:")
                    self.details.append(self.gender)
                    self.age=int(input("Enter your age:"))
                    self.details.append(self.age)
                    self.details.append(self.ticket_price)
                    self.phone_no=int(input("Enter your phone no:"))
                    self.details.append(self.phone_no)
                    tups=tuple(self.bookseat)
                    tupd=tuple(self.details)
                    self.user_deets[tups]=tupd
                    mycursor.execute("Insert into bookedby (s_row,s_col,name,gender,age,ticket_price,phone_no) values (%s,%s,%s,%s,%s,%s,%s);",self.details)
                    cn.commit()
                    print("Booked Successfully!!!!\n")
                    self.details.clear()
                else:
                    print("Ok see you soon!!!")
                    self.details.clear()
                print("1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show Booked Tickets User Info \n0. Exit")
                self.option=int(input())

            
            elif self.option==3:
                mycursor.execute("select count(*) from bookedby;")
                val=mycursor.fetchone()
                print("Number of tickets purchased:",val[0])
                print("Percentage of tickets booked:","{:.2f}".format((val[0]/(self.row*self.column))*100),"%")
                if self.row*self.column>60:
                    print("Current income: $",10,"and $",8)
                else:
                    print("Current income: $",10)
                if self.row*self.column>60:
                    print("Total Income: $",(((self.row//2)*self.column)*10)+((self.column*(self.row-(self.row//2)))*8),"\n")
                else:
                    print("Total Income: $",((self.row*self.column)*10),"\n")
                print("1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show Booked Tickets User Info \n0. Exit")
                self.option=int(input())

            elif self.option==4:
                op=input("Enter the row and column by using comma:").split(",")
                tup=tuple(op)
                for deets in self.user_deets:
                    if deets==tup:
                        print("Name:",self.user_deets[deets][2])
                        print("Gender:",self.user_deets[deets][3])
                        print("Age:",self.user_deets[deets][4])
                        print("Ticket Price:",self.user_deets[deets][5],"$")
                        print("Phone Number:",self.user_deets[deets][6])
                        
                print("1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show Booked Tickets User Info \n0. Exit")
                self.option=int(input())

            elif self.option==0:
                print("Thanks for visiting see you soon!!!!!!!")
                mycursor.execute("TRUNCATE TABLE bookedby;")
                cn.commit()
                break
            else:
                print("Please choose from the options given below\n")
                print("1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show Booked Tickets User Info \n0. Exit")
                self.option=int(input()) 

    
        
ob=Interaction()






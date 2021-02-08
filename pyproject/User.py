from Super import Super
class User:
    user={}
    marks=0
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    
    def takeupquiz(self):
        choose=input("\n\nEnter the quiz you want to take(science/maths):")
        level=input("\nEnter the difficulty level you want (easy/hard):")
        if choose.lower()=='science' and level.lower()=='easy':
            for val in Super.science_q_e:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":", Super.options[val][i])
                ans=input()
                if Super.science_q_e[val]==ans:
                    User.marks+=2
                    User.user[self.roll_no]=User.marks

        elif choose.lower()=='science' and level.lower()=='hard':
            for val in Super.science_q_h:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":", Super.options[val][i])
                ans=input()
                if Super.science_q_h[val]==ans:
                    User.marks+=5
                    User.user[self.roll_no]=User.marks

        elif choose.lower()=='maths' and level.lower()=='easy':
            for val in Super.maths_q_e:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":", Super.options[val][i])
                ans=input()
                if Super.maths_q_e[val]==ans:
                    User.marks+=2
                    User.user[self.roll_no]=User.marks

        elif choose.lower()=='maths' and level.lower()=='hard':
            for val in Super.maths_q_h:
                print(val)
                for i in range(len(Super.options[val])):
                    print(str(i+1) + ":", Super.options[val][i])
                ans=input()
                if Super.maths_q_h[val]==ans:
                    User.marks+=5
                    User.user[self.roll_no]=User.marks
        

    def result(self):
        print("\n***Result***\n")
        print("***Easy quiz contains questions for 2 marks each***")
        print("***Hard quiz contains questions for 5 marks each***\n")
        res=int(input("enter your rollno:"))
        
        print(self.name,"has obtained",User.user[res],"marks")
        User.marks=0
        print("\nright options for the questions were:")
        for val in Super.science_q_e.values():
            print(val)
        for val in Super.science_q_h.values():
            print(val)
        for val in Super.maths_q_e.values():
            print(val)
        for val in Super.maths_q_h.values():
            print(val)
                
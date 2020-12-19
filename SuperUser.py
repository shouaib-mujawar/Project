class SuperUser:
	question=[]
	answer=[]
	total=0
	def __init__(self,su_id,name):
		self.su_id=su_id
		self.name=name
		self.su_user={}
		self.su_user[su_id]=name
		
	def add_question(self,ques, answer):
		SuperUser.question.append(ques)
		SuperUser.answer.append(answer)
		SuperUser.total += 1


class User(SuperUser): 
	nm_user={}	
	marks=0	

	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
		User.nm_user[rollno]=name
	
		
	def solve(self):
		print("Each Question carries one mark\n") 
		for i in SuperUser.question:
			print(i)
			ans=input()
		for y in SuperUser.answer:
			if y==ans:
				User.marks += 1
				
	def displayresult(self):
		print("\nyou've scored",User.marks,"out of",User.total)


	
ob=SuperUser(1,"John")
ob.add_question('What color are apples?\n(a)Red/Green\n(b)Orange', "a")
ob.add_question('What color are orange?\n(a)Purple\n(b)Orange', "b")
ob.add_question('What color are pineapple?\n(a)Yellow\n(b)Blue', "a")
ob.add_question('What color are mango?\n(a)Red Yellowish\n(b)Orange', "a")
ob.add_question('Unit of electric power may also be expressed as\n(a) volt ampere\n(b) kilowatt hour\n(c) watt second\n(d) Joule second',"a")
ob.add_question('Electrical resistivity of a given metallic wire depends upon\n(a) its length\n(b) its thickness\n(c)  its shape\n(d)  nature of the material',"d")
ob.add_question('Kilowatt hour is the unit of\n(a) power\n(b) energy\n(c) impulse\n(d) force',"b")
ob.add_question('The unit of specific resistance is\n(a) ohm\n(b) ohm-metre\n(c) ohm per metre\n(d) mho',"b")

ob=User(1,"h")
ob.solve()
ob.displayresult()


# ob=User(2,"m")
# ob.solve()
# ob.displayresult()
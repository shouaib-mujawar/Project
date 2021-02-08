class Super:
    science_q_e={}
    science_q_h={}
    maths_q_e={}
    maths_q_h={}
    options={}
    s_user={}    
    def __init__(self,s_id,s_name):
        self.s_id=s_id
        self.s_name=s_name
        print("hey",s_name,"you can set the quiz")

    def setquestion(self):
        while True:
            quiz=input("Do you want to set quiz on some other topic?(y/n)")
            if (quiz.lower()=='y'):
                topic=input("Enter the topic you want to set the quiz on (Science/Maths):")
                difficulty=input("\nEnter the difficulty level of quiz(easy/hard):")
                    
                if topic.lower()=='science' and difficulty.lower()=="easy":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.science_q_e[question]=answer
                        
                elif topic.lower()=='science' and difficulty.lower()=="hard":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.science_q_h[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="easy":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.maths_q_e[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="hard":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.maths_q_h[question]=answer
            else:
                break
    
    def add_question(self):
        while True:
            add_q=input("Do you want to add question(y/n)")
            if add_q.lower()=='y':
                topic=input("Enter the topic where you want your question to be added (Science/Maths):")
                difficulty=input("\nEnter the difficulty level of the question (easy/hard):")
                    
                if topic.lower()=='science' and difficulty.lower()=="easy":
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.science_q_e[question]=answer
                
                elif topic.lower()=='science' and difficulty.lower()=="hard":
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.science_q_h[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="easy":
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.maths_q_e[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="hard":
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.maths_q_h[question]=answer
            else:
                break


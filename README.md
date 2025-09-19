# 100-days-of-coding
i will ake coding a habit.

def user_choice():
    choice='wrong'
    acceptable_range=range(0,10)
    within_range=False 
    while choice.isdigit()==False or within_range==False:
         choice=input("please enter a number between 0-10:")
         #digit check
         if choice.isdigit()== True:
             if int(choice) in acceptable_range:
                 within_range= True
             else:
                 print("sorry you are out of acceptable range")
                 within_range =   False
                     
    
    return int(choice)  
user_choice()


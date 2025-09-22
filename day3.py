#Day 3
game_list=[0,1,2]
def display_game(game_list):
    print("here is the game list:")
    print(game_list)
    
def position_choice():
    choice='wrong'
    while choice  not in game_list['0','1','2']  :    
        choice=input("pick a postion 0,1,2")
        if choice not in ['0','1','2']  :
            print("sorry the input is not valid")
    return int(choice)        
def replacmeant_choice(game_list,position):
    user_placement=input("enter the string to replace the number")
    game_list[position]=user_placement
    return game_list()
def gameon_choice(y,N):
    choice='dont'
    while choice  not in["y","N"]:
     choice= input("choose y or n for playing and not playing game further:")
     if choice not in["y","N"]:
         print("sorry invalid syntext")
    if choice =="y":
        return(game_list)
    else:
        return("Game over")     
    

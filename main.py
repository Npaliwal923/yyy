#stone paper scisser
import random
def game(computer,player):
    #if two values are equal, declare it is tie
    if computer == player:
        return None 
   
    #all possiblity with stone "s"
    elif computer == "s":
        if player == "p":
            return True
        elif player== "sic":
            return True     

    #all possiblity with stone paper "p"
    elif computer == "p":
        if player == "s":
            return False
        elif player =="sic":
            return True

    #all possiblity with scisser "sic"
    elif computer == "sic":
        if player == "s":
            return False
        elif player =="p":
            return False 
print("computer turn - stone(1),paper(2)and scisser(3)")
random_no = random.randint(1,3) 
#print(random_no) #computer chose random number 
if random_no == 1:
    computer = "s"
elif random_no == 2:
    computer = "p"
elif random_no == 3:
    computer = "sic"
 
player = input("player turn - stone(1),paper(2)and scisser(3) ")
a = game(computer,player)  


print("computer chose ", computer)
print("player chose ",player)    


if a == None:
    print("the game is draw ")
elif a :
    print("Player = win ")
else:
    print("player = lose")
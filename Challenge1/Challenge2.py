import random

choices =["rock","papper","scissors"]
chance = 3
user_score = 0
computer_score =0
while chance >0:
    computer_choice = random.choices(choices)
    print(str(computer_choice[0]))
    print("--------------------------------------")
    print("1. rock")
    print("2. papper")
    print("3. scissors")
    print("--------------------------------------")
    user_choice_num = int(input("Enter you number of choice: "))
    if user_choice_num<1 or user_choice_num>3:
        print("Please choose the correct choice!!")
        continue
    user_choice = choices[user_choice_num-1]
    if user_choice==computer_choice[0]:
        print("Oops we think the same thing!!")
    elif user_choice == "rock" and computer_choice[0] == "papper" or user_choice == "papper" and computer_choice[0] == "scissors" or user_choice=="scissors" and computer_choice[0] == "rock":
        print("You lose")
        computer_score += 1
    else: 
        print("You win ")
        user_score += 1

    if(chance == 1):
        if(user_score == computer_score):
            chance +=1
        
    
    # status = "Tile" if computer_choice == user_choice else "You win!" if (user_choice,computer_choice) in [("rock","scissors"),("paper","rock"),("scissors","paper")] else "You lose!"
    # print(status)
    chance -=1
print("User score",user_score)
print("Computer score",computer_score)
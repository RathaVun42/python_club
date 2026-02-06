import random
randomNum = random.randint(1,10) # this will be random the number from 1 to 10
your_choice = int(input("Please enter your number "))
chance = 1
while your_choice!=randomNum:
    chance +=1
    your_choice = int(input("Please enter your number "))
    if(your_choice == randomNum):
        print("Good job the random number is ", randomNum)
        break
    if(chance == 3):
        print("You don't have another chance):")
        break
    


    

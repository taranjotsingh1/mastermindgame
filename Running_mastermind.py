# This file to call the methods and functions
import Mastermind_game # importing the mastermind game code
import time # to give a real look and put little pose.
# Printing the game name 
name = "----MasterMind------"
decoration = "-" * 80 # decorating around the name
print(decoration)
print("\n" * 3)

print(" " * 30, name)
print("\n" * 3)

print(decoration)
print()
# Assiging the player to resue in all the files
player2 = Mastermind_game.Code_breaker() 
player1 = Mastermind_game.Code_maker() 

choice = ["p", "c"]
permission = input("Do you want to play with person or computer. please enter[p or c]: ").lower() # Asking for input
# Making sure the permission in according to instructions
while permission not in choice or type(permission) == int:
    print("it has to be p or c")
    permission = input("Do you want to play with person or computer. please enter[p or c]: ").lower()
# if two people wants to play toghter
if permission.lower() == "p":
    maker_list = player1.person_code_maker()# Asking code maker to make a list, calling function
    print()# printing empty space to hide the the code makers code
    print('\n' * 10)

    while player2.win == False and player1.win == False: # till it decided who won
        player2.attempt += 1 # counting the attempts till it reaches the number of rows
        print("Now code breaker Turn to guess the colours")
        print('\n' * 3)
        print("Loading the list for Code breaker.")
        print()
        time.sleep(0.6)# wait for 0.6 second

        breaker_list = player2.person_code_breaker()# Asking for breaker to make list
        points = player2.give_feedback(breaker_list, maker_list) # giving feed back to code breaker
        # code brekers win
        if points == 4: # if points are 4 it means code breaker wins 
            print("Congrats Code breaker, you have match the Code makers mind")
            print("Code breaker has won")
            player2.win = True
        # if code makers win
        elif player2.attempt == player2._rows: # if attempts reaches equal to rows
            print( "Code breaker has lost.")
            print("Code makers Scores:", player1.code_maker_score)
            player1.win = True
        # Calculating code makers points
        elif points != 4:
                player1.code_maker_score += (4 - points)

# if person choose to play with computer
elif permission.lower() == "c":
    # Giving choice to be code breaker or code maker
    another_choice = int(input("Do you want to be (1) code_breaker or (2) code_maker, enter[1 or 2]: "))
    int_choice =[1, 2]
    while another_choice not in int_choice or type(int_choice) == str: # making sure choice is 1 or 2
        print("It has to be 1 or 2. Please try again.")
        another_choice = int(input("Do you want to be (1) code_breaker or (2) code_maker, enter[1 or 2]: "))
    if another_choice == 1:
        computer_list = player1.computer_code_maker()
        print()
        print("Computer has decided the list.")
        while player2.win == False and player1.win == False: # loop to till decided who win

            player2.attempt += 1 # Calculating attempts of code breaker
            print()
            print("Loading the list for Code breaker.")
            print()
            time.sleep(0.6)
            breaker_list = player2.person_code_breaker() # making breakers list 
            points = player2.give_feedback(breaker_list, computer_list) # giving feed back and calculating points
            if points == 4: # if points are 4 it means code breaker wins 
                print("Congrats Code breaker, you have match the Code makers mind")
                print("Code breaker has won")
                player2.win = True
            elif player2.attempt == player2._rows:
                print( "Code breaker has lost.")
                print("Computer Scores:", player1.code_maker_score)
                player1.win = True
            elif points != 4: # Giving scores to code maker
                player1.code_maker_score += (4 - points)
    elif another_choice == 2:
        maker_list = player1.person_code_maker()
        print('\n' * 4)
        
        while player2.win == False and player1.win == False: 
            player2.attempt += 1
            print()
            print("Loading the list for Computer to choose.")
            print()
            time.sleep(1)
            breaker_list = player2.computer_code_breaker()
            print()
            print("Computer list is: ", breaker_list)
            points = player2.give_feedback(breaker_list, maker_list)# printing feedback of computer's guess
            if points == 4: # if points are 4 it means code breaker wins 
                print("Computer has matched the Code makers mind")
                print("computer has won")
                player2.win = True # changing the code breakers win true 
            elif player2.attempt == player2._rows: # if attempts reaches equal to rows 
                print( "computer has lost.")
                print("You Score:", player1.code_maker_score)
                player1.win = True # changing the code maker win true
            elif points != 4: # Giving score to code maker
                player1.code_maker_score += (4 - points)

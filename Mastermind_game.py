import random
class Mastermind:
    # Setting up dict of colors.
    code_maker_colours = {1 : "RED", 2 : "GREEN", 3:"YELLOW", 4:"BLUE", 5:"BLACK", 6:"ORANGE"}
    code_maker_score = 0 # initial scores for code maker

    def __init__(self):
        self._rows = 10 # rows of the Mastermind
        self.win = False # to decide the win
        self.attempt = 0 # to calculate the attempts
    
    # to print the colour of the choice and resue the code
    def colour_choice (self, colour_code, dict = {}):
        for number, colour in dict.items():
            if colour_code == number:
                return colour
    # to shuffle the colours of the list of code breaker and reuse the code
    def code_breaker_colours(self):
        print("Shuffling the list of Colours.")
        colours = list(Mastermind.code_maker_colours.values())
        random.shuffle(colours)
        resetting_dict = dict(zip(Mastermind.code_maker_colours, colours))
        return resetting_dict
    
    # To give the feedback to code breaker
    def give_feedback(self, code_breaker_list = [], code_maker_list = []):
        right_pick_colour = 0 # to  present the right choosen colours
        wrong_pick_colour = 0 # To present the wrong choosen colours
        # going over the code breaker list
        for colours in code_breaker_list:
            if colours in code_maker_list:
                right_pick_colour += 1
            elif colours not in code_maker_list:
                wrong_pick_colour += 1

        print("Right colours", " " , right_pick_colour , '\n', "wrong colours" , " " , wrong_pick_colour)
        return right_pick_colour

# Code maker is inheritance from Mastermind
class Code_maker(Mastermind):
    # if two people wants to play 
    def person_code_maker(self):
        # printing the space and the instructions
        print() 
        print(" " * 10, "Colour codes for Code maker.")
        print()
        print(Mastermind.code_maker_colours) # printing colour codes for code maker
        print()
        # Asking for first colour
        first_number = int(input("please enter number of the color you want to choose first between(1-6): "))
        while first_number not in Mastermind.code_maker_colours or type(first_number) == str: # making sure the colour choose in right way.
            print("number has to be in colour codes")
            first_number = int(input("please enter number of the color you want to choose first(1-6): "))
        if first_number in Mastermind.code_maker_colours: # getting colour from dictionary
            first_colour = self.colour_choice(first_number, Mastermind.code_maker_colours)
        # Asking for secong colour  
        second_number = int(input("please enter number of the color you want to choose second: "))
        while second_number not in Mastermind.code_maker_colours:
            print("number has to be in colour codes")
            second_number = int(input("please enter number of the color you want to choose second: "))
        if second_number in Mastermind.code_maker_colours:
            second_colour = self.colour_choice(second_number, Mastermind.code_maker_colours)
        # Asking for third number    
        third_number = int(input("please enter number of the color you want to choose third: "))
        while third_number not in Mastermind.code_maker_colours:
            print("number has to be in colour codes")
            third_number = int(input("please enter number of the color you want to choose third: "))
        if third_number in Mastermind.code_maker_colours:
            third_colour = self.colour_choice(third_number, Mastermind.code_maker_colours)
        # Asking for fourth number   
        fourth_number = int(input("please enter number of the color you want to choose fourth: "))
        while fourth_number not in Mastermind.code_maker_colours:
            print("number has to be in colour codes")
            fourth_number = int(input("please enter number of the color you want to choose fourth: "))
        if fourth_number in Mastermind.code_maker_colours:
            fourth_colour = self.colour_choice(fourth_number, Mastermind.code_maker_colours)
        
        person_colour_list = [first_colour, second_colour, third_colour, fourth_colour]
        return person_colour_list
   
    # if person wants to play with computer as code maker
    def computer_code_maker(self):
        # choosing the random number 
        first_number = random.randint(1 , 6)
        first_colour = self.colour_choice(first_number, Mastermind.code_maker_colours) # choosing the colour accordingly
        # choosing the second random number
        second_number = random.randint(1, 6)
        second_colour = self.colour_choice(second_number, Mastermind.code_maker_colours) # choposing the colour accordingly
        # choosing the third number
        third_number = random.randint(1, 6)
        third_colour = self.colour_choice(third_number, Mastermind.code_maker_colours)
        # choosing the fourth number
        fourth_number = random.randint(1, 6)
        fourth_colour = self.colour_choice(fourth_number, Mastermind.code_maker_colours)
        
        colour_list = [first_colour, second_colour , third_colour , fourth_colour]
        return colour_list

class Code_breaker(Mastermind):
    
    def person_code_breaker(self):
        colour_list_for_breaker = self.code_breaker_colours() # to make shuffle list
        print(colour_list_for_breaker) 
        # Asking for first colour
        first_number = int(input("Please enter the first number of colour of your choice: "))
        while first_number not in colour_list_for_breaker:
            print("Number has to be between 1-6")
            first_number = int(input("Please enter the first number of colour of your choice: "))
        if first_number in self.code_breaker_colours():
            first_colour = self.colour_choice(first_number, colour_list_for_breaker)
            print("You choose", first_colour)
        # Asking for second colour
        second_number = int(input("Please enter the second number of colour of your choice: "))
        while second_number not in colour_list_for_breaker:
            print("Number has to be between 1-6")
            second_number = int(input("please enter the second number of colour of your choice: "))
        if second_number in colour_list_for_breaker:
            second_colour = self.colour_choice(second_number, colour_list_for_breaker)
            print("Your second colour:", second_colour)
        # asking for third colour
        third_number = int(input("Please enter the third number of colour of your choice: "))
        while third_number not in colour_list_for_breaker:
            print("Number has to be between 1 to 6")
            third_number = int(input("please enter the third number of colour of your choice: "))
        if third_number in colour_list_for_breaker:
            third_colour = self.colour_choice(third_number, colour_list_for_breaker)
            print("Your third choice of colour:", third_colour)
        # Asking for fourth colour
        fourth_number = int(input("please enter number of the color you want to choose fourth: "))
        while fourth_number not in colour_list_for_breaker:
            print("number has to be in colour codes")
            fourth_number = int(input("please enter number of the color you want to choose fourth: "))
        if fourth_number in colour_list_for_breaker:
            fourth_colour = self.colour_choice(fourth_number, colour_list_for_breaker)
            print("Your fourth colour:", fourth_colour)
        
        colour_list = [first_colour, second_colour, third_colour, fourth_colour]
        return colour_list
    
    # if user wants to be code maker not breaker
    def computer_code_breaker(self):
        colour_list_for_breaker = self.code_breaker_colours()
        print(colour_list_for_breaker)
        # choosing the random number 
        first_number = random.randint(1 , 6)
        first_colour = self.colour_choice(first_number, colour_list_for_breaker) # choosing the colour accordingly
        # choosing the second random number
        second_number = random.randint(1, 6)
        second_colour = self.colour_choice(second_number, colour_list_for_breaker) # choposing the colour accordingly
        # choosing the third number
        third_number = random.randint(1, 6)
        third_colour = self.colour_choice(third_number, colour_list_for_breaker)
        # choosing the fourth number
        fourth_number = random.randint(1, 6)
        fourth_colour = self.colour_choice(fourth_number, colour_list_for_breaker)
        
        colour_list = [first_colour, second_colour , third_colour , fourth_colour]
        return colour_list













            


            
import random, os
from time import sleep

class number_guessing:
    def __init__(self,mode):
        self.mode = mode
        self.answer = self.__select_number(self.mode)
    
    def __select_number(self, mode):
        self.number = 0
        if mode == 1:
            self.number = random.randint(1, 10)
        elif mode == 2:
            self.number = random.randint(1, 100)
        elif mode == 3:
            self.number = random.randint(1, 1000)
        elif mode == 4:
            self.number = random.randint(1, 10000)
        return self.number
    
    def no_of_tries(self, mode):
        self.count = 0
        if mode == 1:
            self.count = 3
        elif mode == 2:
            self.count = 6
        elif mode == 3:
            self.count = 9
        elif mode == 4:
            self.count = 12
        return self.count

    def verify(self, guess):
        if guess == self.answer:
            return True
        else:
            #message = "Alas! The number you guessed is wrong"        
            return False

    def waiting(self):
        print("Let us think of a number")
        print("<(^_^)>")
        sleep(0.5)
        os.system("cls")
        print("<(-_-)>")
        sleep(0.5)
        os.system("cls")
        print("<(^_^)>")
        sleep(0.5)
        os.system("cls")
        print("<(-_-)>")
        sleep(0.5)
        os.system("cls")
        print("<(^_^)>")
        sleep(0.5)
        os.system("cls")
        print("<(-_-)>")
        sleep(0.5)
        os.system("cls")
        print("<(^_^)>")
        sleep(0.5)
        os.system("cls")
        print("<(-_-)>")
        sleep(0.5)
        os.system("cls")
        print("<(^_^)>")
        sleep(0.5)
        os.system("cls")
        print("<(-_-)>")
        os.system("cls")
        print("We got it.")
        sleep(1)

def print_heading():
    print (
'''
-----------------------------------------------------------------------
Welcome to the Number guessing Game.
You will have 4 modes and For each mode
You will have a fixed number of tries to guess.

 Number           Mode            Tries 
     1            Beginner            3
     2            Intermediate        6
     3            Hard                9
     4            Expert             12

Please enter your choice accordingly.
We hope you injoy the game.
Happy Guessing!
---------------------------------------------------------------------
''')


play_more = True
while play_more:
    print_heading()
    try:
        choice = int(input("Enter the mode number (1/2/3/4): "))
        game = number_guessing(choice)
        game.waiting()
        trying = game.no_of_tries(choice)
        print("You have {} number of tries.".format(trying))
        for _ in range(trying):
            try:
                guess = int(input("Enter your guess: "))
                if game.verify(guess):
                    message = "Congratulations! You guessed the no. right"
                    break
                else:
                    print("Alas! You were wrong. ")
                    print("You have {} tries left".format(trying))
            except ValueError:
                print("Sorry! You entered a wrong input")
        response = input("Do you want to play more? (y/n)")
        if response.lower() == "y" or response.lower() == "yes":
            os.system("cls")
            play_more = True
        else:
            play_more = False
            print("Thank you for playing. We hope you had fun!")
    except ValueError:
        print("Sorry! You entered a wrong input")
        print("Quitting ...")
from secrets import choice

class rps:
    def __init__(self, user):
        self.options = ["R", "P", "S"]
        self.cpu_score = 0
        self.user_score = 0
        self.player1 = "CPU"
        self.player2 = user
    
    def is_valid(self,user_response):
        if user_response in self.options or user_response == "E" or user_response == "Q":
            return True
        else:
            print ("Sorry! Wrong input")
            return False

    def cpu_chance(self):
        return choice(self.options)
    
    def winner(self, cpu_response, user_response):
        if user_response == cpu_response:
            print("Tie!")
            self.cpu_score += 1
            self.user_score += 1
        elif user_response == "R":
            if cpu_response == "P":
                print("CPU wins!", cpu_response, "covers", user_response)
                self.cpu_score += 1
            else:
                print("You win!", user_response, "smashes", cpu_response)
                self.user_score += 1
        elif user_response == "P":
            if cpu_response == "S":
                print("CPU wins!", cpu_response, "cut", user_response)
                self.cpu_score+=1
            else:
                print("You win!", user_response, "covers", cpu_response)
                self.user_score += 1
        elif user_response == "S":
            if cpu_response == "R":
                print("CPU wins!", cpu_response, "smashes", user_response)
                self.cpu_score+=1
            else:
                print("You win!", user_response, "cut", cpu_response)
                self.user_score += 1
        elif user_response == "E" or user_response == "Q":
            self.print_result()
            return False
        return True
    
    def print_result(self):
        print("\nFinal Scores:")
        print(f"{self.player1}:{self.cpu_score}")
        print(f"{self.player2}:{self.user_score}")
        if self.user_score >= self.cpu_score:
            print(f"Congratulations {self.player2} wins!")
        else:
            print(f"Congratulations {self.player1} wins!")

def welcome():
    print(
'''
-----------------------------------------------------------------------
Welcome to the Rock | Paper | Scissor game
You are playing against our intelligent CPU ;)
you have to enter your choices accordingly :
R -> Rock
P -> Paper
S -> Scissor
E or Q -> End the game
Please enter your choices accordingly
We hope you injoy the game.
Happy Guessing!
---------------------------------------------------------------------
'''
)

welcome()
username = input("Enter your name: ")
game = rps(username)
play_more = True
while play_more is True:
    print("Enter your choice below. R | P | S")
    user_choice = input().upper()
    cpu_choice = game.cpu_chance()    
    if game.is_valid(user_choice):        
        play_more = game.winner(cpu_choice, user_choice)
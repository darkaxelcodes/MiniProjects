from secrets import choice
class password:
    def __init__(self, l_alphabets, u_alphabets, numbers, special_characters,username, length):
        self.password = self.__generate_password(l_alphabets, u_alphabets, numbers, special_characters, username, length)
    
    def __generate_password(self, l_alphabets, u_alphabets, numbers, special_characters,username, length=15):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXY"
        num = "0123456789"
        special = "@$#%^&*()"
        password = ""
        if u_alphabets:
            temp = ""
            for _ in range(length):
                temp += choice(upper)
            password += temp
        if l_alphabets:
            temp = ""
            for _ in range(length):
                temp += choice(lower)
            password += temp
        if numbers:
            temp = ""
            for _ in range(length):
                temp += str(choice(num))
            password += temp
        if special_characters:
            temp = ""
            for _ in range(length):
                temp += choice(special)
            password += temp
        password = username[0] + password + username[-1]
        final = ""
        for _ in range(length):
            final += choice(password)
        return final

def welcome():
    print (
'''
This is the password generator.
You have 4 options to set as True/False
1. lowercase
2. uppercase
3. numbers
4. sppecial characters
You can also choose to define the length of the password (default = 15)
---------------------------------------------------------------------
''')

welcome()
print("Enter your choices as y/n")
l_alphabets = input ("Do you want lower alphabets? (y/n) ")
if l_alphabets.lower() == 'y':
    l_alphabets = True
else:
    l_alphabets = False

u_alphabets = input ("Do you want capital alphabets? (y/n) ")
if u_alphabets.lower() == 'y':
    u_alphabets = True
else:
    u_alphabets = False

numbers = input ("Do you want numbers? (y/n) ")
if numbers.lower() == 'y':
    numbers = True
else:
    numbers = False

special_characters = input ("Do you want special characters? (y/n) ")
if special_characters.lower() == 'y':
    special_characters = True
else:
    special_characters = False

username = input("Enter your username: ")

length = int(input ("Enter the length of the password, Leave blank if you want (default:15): "))
if length != '':
    length = length

pwd = password(l_alphabets, u_alphabets, numbers, special_characters, username, length)
print("Your password is : {}".format(pwd.password))
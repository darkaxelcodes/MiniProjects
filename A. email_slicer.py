import re
emails = input("Enter Your Email: ").strip()
emails = re.findall("([a-zA-Z0-9_.-a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", emails)
if len(emails) == 0:
    print("Sorry! The email is in wrong format")
else:
    for email in emails:        
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]
        print ("The username is - {}".format(username))
        print ("The domain for this username is - {}".format(domain))    
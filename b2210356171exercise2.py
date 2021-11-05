email=input("The string to check: ")
atsign='@'
dot='.'
def check_the_email(email):
    if atsign in email:
        if dot in email:
            return True
        else:
            return False
    else:
        return False

print(check_the_email(email))
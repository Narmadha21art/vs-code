import re

def check_password_strenght(password):
    if len(password) <8:
        return "weak: password must be 8 characters long."
    if not any(char.isdigit() for char in password):
        return "weak:password must include at least one number."
    if not any(char.isupper() for char in password):
        return "weak: password must include at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "weak:password must include lowercase letters."
    if not re.search(r'[!@$#%^&**()><?]',password):
        return "medium:Add special character to make you're password strong."
def  password_checker():


    print("welcome to the password strenght checker!")

    while True:
        password = input("\nEnter you're password (or type 'exit' to quit):")

        if password.lower()=="exit":
            print("Thank you for using the password strenght checker")
            break

        result = check_password_strenght(password)
        print(result)

#run the password strenght checker
#if_name_==
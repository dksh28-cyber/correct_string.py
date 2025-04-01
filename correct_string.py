def name_func():
    while True:
        name = input("Enter your full name: ")
        if name.isalpha():
            return name
        print("use only characters")
        
def age_func():
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            return age
        print("enter numbers only.")

def email_func():
    while True:
        email = input("Enter your email: ")
        if "@" in email and email.endswith(".com"):
            return email
        print("enter a valid email with '@ and .com'")

username = name_func()
userage = age_func()
useremail = email_func()






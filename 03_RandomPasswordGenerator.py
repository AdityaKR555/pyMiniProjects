import random

options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$%&"
password = ""

length = int(input("Enter the length of password: "))

if length>10 or length<4:
    print("Length should be in range 4 to 10")
    exit()

else:
    for i in range(length):
       nextChar = random.choice(options)
       password = password + nextChar
    
print("Your Password is: ", password)

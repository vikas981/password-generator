import random
length=input("Password Length?: ")
length=int(length)
number=input("Number of Password?: ")
number=int(number)
chars="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%&*(+=}?,;"
for p in range(number):
    password=''
    for c in range(length):
        password +=random.choice(chars)
    print(password)

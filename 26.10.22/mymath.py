import random 

def read_number():
    x = int(input("enter integer number from 1 to 9: "))
    return x

def generate_number():
    a = random.randint(1, 10)
    return a
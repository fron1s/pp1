import mymath

AI_number = mymath.generate_number()
user_number = mymath.read_number()

while user_number != AI_number:
    AI_number = mymath.read_number()

print("You won!")    
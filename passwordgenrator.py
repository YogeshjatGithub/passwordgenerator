import random

letter=["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=[1,2,3,4,5,6,7,8,9,0]
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']

min_letters=int(input("Enter the minimum number of letters : "))
min_numbers=int(input("Enter the minimum number of numbers : "))
min_special_characters=int(input("Enter the minimum number of special characters : "))
password: str=""
for x in range(0,min_letters):
    password+=random.choice(letter)

for y in range(0,min_numbers):
    password+=str(random.choice(numbers))

for z in range(0,min_special_characters):
    password+=random.choice(special_characters)
password=list(password)

random.shuffle(password)

password = "".join(map(str, password))


print(f"The password we suggest you to use is : {password} ")


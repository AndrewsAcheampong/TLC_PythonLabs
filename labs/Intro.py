import random 

# QUESTION 1

num = (int)(input("Enter your favorite number : "))

if num % 2 == 0:
    print("The number is an even number")

else: 
    print("The number is an odd number")


# QUESTION 2

firstName = "Andrews"
lastName = "Acheampong"
fullName = firstName + " " + lastName

print(firstName)
print(lastName)
print(fullName)


# QUESTION 3
G_number = random.randint(1, 10); 
print(G_number)


while True:
    guess = (int)(input("Guess any number: "));

    if guess == G_number:
        print("Hurray!! you've found the number")
        break
    else:
        continue



# QUESTION 1

numbers = (int)(input("Enter any number : "))

if numbers % 2 == 0:
    print("The number is an Even number")
else:
    print("The number is an odd number")
    
# ----------------------------------------------------------------------------------------------

# QUESTION 2

fullName = "Acheampong Andrews"
age = str(23)

print(fullName)
print(age)

nameAge = fullName + " is " + age + " years old"
print(nameAge)

# ----------------------------------------------------------------------------------------------

# QUESTION 3
# A
lists = [1,4,9,16,25]

for i in lists:
    if i % 2 == 0:
        print(i , " is an even number")

# B
tuples = (1 , 4, 9, 16, 25)

for i in lists:
    if i % 2 == 0:
        print(i , " is an even number \n")

# ----------------------------------------------------------------------------------------------
# QUESTION 4

years = 25
sum = 0
count = 0

while years > 0:
    sum = sum + years
    count += 1
    print("Year " + str(count) + " = " , sum)
    years -=1
    
print(count , " years \n")

# ----------------------------------------------------------------------------------------------

# QUESTION 5

a = 5
print(type(a))

b = 5000 * 50000000
print(type(b))

c = 'j'
print(type(c))

d = 1j
print(type(d))

e = (1,)
print(type(e))

f = [1]
print(type(f))

g = None
print(type(g))

print("\n")

# QUESTION 6

# Decimal(".1")

# ----------------------------------------------------------------------------------------------

# QUESTION 7
# FIBONACCI

n = 20
count = 20

while n > 0:
    fib = n-1 + n-2
    print("The " , count , " value for fib is : " , fib)
    count -= 1
    n -= 1

# ----------------------------------------------------------------------------------------------

    count = 0
n1 = 0
n2 = 1

while count < 20:
    print(n1)
    next = n1 + n2  
    n1 = n2
    n2 = next
    count = count + 1
# ----------------------------------------------------------------------------------------------
# QUESTION 8
# A
name = "Andrews"
listOfChar = list(name)
print("\n The last character in the name is : " , listOfChar[-1].upper())

# B
for i in listOfChar:
    print(i ,  end= " : ")

# -----------------------------------------------------------------------------------------------
# QUESTION 9


print('\n')
count= 0
countFive = 0
lists = []

while True:
    
    userInput = (int)(input("Enter a number between 1 and 8 : " ))

    if userInput > 1 and userInput < 8:
        count+=1
        lists.append(userInput)
        print(count)
        
        # Section 9B
        if userInput == 5:
            print("You've entered number 5")
            countFive += 1
            print(countFive)
        
        if count == 11:
            break
    else:
        print("Wrong input, try again!")

    print(lists)
        
# # -----------------------------------------------------------------------------------------------
# QUESTION 10
print("\n")

comprehensions = [1, 4, 9, 16, 25]

listComprehension = [x for x in comprehensions if x % 2 == 1]
print(listComprehension)


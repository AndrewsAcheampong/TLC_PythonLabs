# QUESTION ONE
# # -----------------------------------------------------------------------------------------------
# def inc(x):
#     x = x + 1
#     print(x)
    
# x = 10
# inc(x)

# QUESTION TWO
# # -----------------------------------------------------------------------------------------------
fruits = ['mango' , 'orange' , 'pineapple']
print(fruits)

def swap(list1):
    lastElement =  list1.pop()
    list1.insert(0, lastElement)
    return list1

swap(fruits)

# QUESTION THREE 
# # -----------------------------------------------------------------------------------------------
def tupleGen(list1,indices):
    count = 0
    tup = ()
    while count < len(indices):
        tup = tup + tuple(list1[indices[count]])
        count = count + 1
    return tup
        
o=['a','b','c','d','e']
indices=[1,0,4]
print(tupleGen(o, indices))       

# QUESTION FOUR
# # -----------------------------------------------------------------------------------------------
def namedParam(**kwargs):
    print(kwargs)
    
    
namedParam(Name = 'Andrews' , Age = '12' , Sex = 'Male' , Nationality = 'Ghanaian')

# QUESTION FIVE
# # -----------------------------------------------------------------------------------------------
def tupleAccum(x , *args):
    for i in args:
        sum = x + i
        print(sum)

tupleAccum(3 , (2,3,4,5,6))

print("Hello World")
    


    
    
    



 
    
    



# numbers = [2,3,4,5,6,7,8]

# # all even numbers in the list

# evenNumbers = [number  for number in numbers  if number % 2 == 0]
# print(evenNumbers)

# for number in numbers:
#     if number % 2 == 0:
#         print(number)
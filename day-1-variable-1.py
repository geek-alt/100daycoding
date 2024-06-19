# Program that switches the value stored in the variables a  and  b

a = input("Enter a value for a: ")
b = input("Enter a value for b: ")


a == b
b == a


print("The value for a is " + b)
print("The value for b is " + a)


#The above code is written without looking in internet. It was done 5-6 times to get the result. At first it was written as : "The code above was found while playing with code below":
'''
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")

a = b
b = a
a = b

print(b)
print(a)
'''

# The below code is written from the course for the exercise.


a = input('a: ')
b = input('b: ')

#logic: using a third variable

c = a
a = b
b = c

print (a)
print(b)
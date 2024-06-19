#This program takes Input of a name and return/prints/tell how many characters are there in the name/input

x = input("What is your name?")

print(len([ele for ele in x if ele.isalpha()])) # Found this methond in stackoverflow as it was allowed to use google. It uses Len() function which tells how many words are there inside(-----)
# and this ele for ele in x. we use isalpha to check if characters in user input is alphabets and len to get count on length of list of alphabets.

#Now trying len function again as first it gave number of words from the input.  it was found that first we use same method as below but instead of printing print(len(s)) we only used
#print(len) and second time we used len function two times
'''
s = input("What is your name?")
len(s)
print(len(s))  #This code gave us error and we rewrote 1st code by searching in stackoverflow and below is code written from seeing an example in the course video.
'''

s = input("What is your name? ")
print(len(s)) # this len function will also print the length of character even if they are numbers or any characters. for eg: 23874erger.--ø output: 14

#Below code is written in single line without using variables.

print(len(input("What is your name? "))) #here code runs from last to first , as it first asks user what is your name and it uses len function to count characters
# and print function at last to print length of the input. You have to write code in this order to get correct if you dont want to use a variable.

name = input("What is your name? ")
length = len(name)
print(length)

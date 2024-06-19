#Fix the code below 👇
'''
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")

'''
# Fixed code below 👇

print("Day 1 - String Manupulation") # - This code block has error of missing a quotion mark ("-------")
print('String Concatenation is done with the "+" sign.') #- This code block has error of multiple quotion mark which is confusing while running code as it represent end and beginning of code.
#and it is required to use different openning and closing method by changing ("----") --> as ('----') or changing quotion around + sign as ('+')

print('e.g. print("Hello " + "world")') #- This code block has error of indentaion while it is unnecessary. It is recommended to delete the indentation or space to stick the beginnning of code to the side.
print("New lines can be created with a '\ and n'.") # got "SyntaxWarning: invalid escape sequence '\ ' "  - This  code block has error of multiple beginning of syntax as we write syntax or code of a function
# between (---code here----) brackets. this code block contain multiple opening brackets or it misses one closing bracket.
print("New lines can be created with a backslash and n.") #- This  code block has error of multiple beginning of syntax as we write syntax or code of a function
# between (---code here----) brackets. this code block contain multiple opening brackets or it misses one closing bracket.


#Full ERROR 👇
'''
SyntaxWarning: invalid escape sequence '\ '
  print("New lines can be created with a '\ and n'.") # got "SyntaxWarning: invalid escape sequence '\ ' "  - This  code block has error of multiple beginning of syntax as we write syntax or code of a function
Day 1 - String Manupulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a '\ and n'.
New lines can be created with a backslash and n.

'''
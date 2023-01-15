"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

number = input("Type your numbers and seperate them using only commas :")
number_split = number.split(',')

number_tuple = tuple(number_split)

print(number_tuple)
print(number_split)
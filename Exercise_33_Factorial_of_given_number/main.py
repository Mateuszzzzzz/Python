"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
number = int(input("Write your number: "))

number_new=1
l=[]
while number > 0:
    l.append(str(number))
    number_new = number_new*number
    number=number-1

print(", ".join(l))
print(number_new)
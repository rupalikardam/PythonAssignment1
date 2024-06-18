'''
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Min:", min(lst))
print("Max:", max(lst))
'''

'''
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()
if unit == 'C':
    print("Fahrenheit:", (temp * 9/5) + 32)
elif unit == 'F':
    print("Celsius:", (temp - 32) * 5/9)
else:
    print("Invalid")
'''
'''
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print("Result:", a + b)
elif operator == '-':
    print("Result:", a - b)
elif operator == '*':
    print("Result:", a * b)
elif operator == '/':
    print("Result:", a / b)
else:
    print("Invalid operator")
'''

'''
with open('source.txt', 'r') as src, open('destination.txt', 'w') as dest:
    dest.write(src.read())
'''

'''
string = input("Enter a string: ")
prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")

if string.startswith(prefix):
    print("Starts with prefix")
if string.endswith(suffix):
    print("Ends with suffix")
'''
'''
string = input("Enter a string: ")
print("List of characters:", list(string))
'''
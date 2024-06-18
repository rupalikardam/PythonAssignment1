import string

s = input("Enter a string: ")
s = s.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", s)

lst = list(map(int, input("Enter list elements separated by space: ").split()))
element = int(input("Enter the element to count: "))
print(f"Occurrences of {element}: {lst.count(element)}")

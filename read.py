import csv


file_path = 'import.csv'


with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    
    
    for row in reader:
        
        print(row)

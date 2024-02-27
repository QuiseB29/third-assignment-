

try:
    
    x = 1 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred.")

except ValueError:
    print("Error: Cannot divide a number by a non-numeric value.")


filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    # Silent handling 
    pass






# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns (asterisks in a row)
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1

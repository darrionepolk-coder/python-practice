# Print a picture using nested loops
# Outer loop = rows
# Inner loop = columns inside each row

# This pattern starts with 5 stars and decreases by 1 each row.
for row in range(5, 0, -1):
    for col in range(row):
        print('*', end=' ')
    print()

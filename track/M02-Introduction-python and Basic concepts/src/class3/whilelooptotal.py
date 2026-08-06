# Read the value of n
n = int(input())

# Initialize the total
t = 0

# Calculate the total using a while loop
while n >= 1:
    t = t + n
    n = n - 1

# Display the total
print(f"Total: {t}")
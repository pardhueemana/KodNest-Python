# Read the limit and target
limit = int(input())
target = int(input())

count = 0
total = 0
found = "No"

# Analyze multiples of 3
for i in range(1, limit + 1):
    if i % 3 == 0:
        count += 1
        total += i
        if i == target:
            found = "Yes"

# Display the results
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Target Found: {found}")
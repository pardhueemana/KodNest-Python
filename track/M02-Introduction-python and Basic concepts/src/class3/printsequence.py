# Read the number and word
n = int(input())
w = input()
l = len(w)

# Print the number sequence
print("Numbers:")
for i in range(1, n + 1):
    print(i)

# Print the characters
print("Characters:")
for i in range(l):
    print(w[i])
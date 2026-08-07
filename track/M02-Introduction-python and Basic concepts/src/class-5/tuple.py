name = input()
course = input()
score = int(input())

# Create the tuple
s = (name, course, score)

# Unpack the tuple
s_name, s_course, s_score = s

# Display the unpacked values
print(f"Name: {s_name}")
print(f"Course: {s_course}")
print(f"Score: {s_score}")
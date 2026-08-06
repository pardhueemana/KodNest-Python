# Read marks, attendance and project completion status
m = int(input())
p = int(input())
project = input()

# Check the academic requirements
if m >= 60 and p >= 75 and project == "yes":
    print("Eligible")
else:
    print("Not Eligible")
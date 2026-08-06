n=int(input())
p=0
f=0
t=0
for i in range(n):
    marks=int(input())
    if marks>=40:
        p+=1
    else:
        f+=1
    t+=marks
print(f"Total Marks: {t}")
print(f"Passed Students: {p}")
print(f"Failed Students: {f}")
if f==0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")
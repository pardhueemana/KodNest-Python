a=int(input())
p=0
n=0
z=0
t=0
for i in range(a):
    b=int(input())
    if b>0:
        p+=1
    elif b<0:
        n+=1
    else:
        z+=1
    t+=b
print(f"Positive Count: {p}")
print(f"Negative Count: {n}")
print(f"Zero Count: {z}")
print(f"Total : {t}")
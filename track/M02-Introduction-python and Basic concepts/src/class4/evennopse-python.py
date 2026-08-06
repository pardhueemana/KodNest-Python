n=int(input())
t=0
while n>=1:
    if n%2==0:
        t=t+n
    n=n-1
print(f"Even Sum: {t}")
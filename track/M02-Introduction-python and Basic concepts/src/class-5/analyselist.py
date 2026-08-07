n=int(input())
sc=[]
for i in range(n):
    sc.append(int(input()))
se=int(input())
h=max(sc)
l=min(sc)
t=sum(sc)
print(f"Highest Score: {h}")
print(f"Lowest Score: {l}")
print(f"Total Score : {t}")
s="Not Found"
for i in sc:
    if i==se:
        s="Found"
print(f"Search Result: {s}")

a=input()
n=len(a)
p=[]
for i in range(0,n):
    b=a[:]
    b=b[0:i]+b[i+1:]
    p.append(b)
#m=min(p)
#k=int(m)
#print(k)
print(p)

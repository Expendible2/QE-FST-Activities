l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in l1:
    if(i%2!=0):
        l.append(i)
for i in l2:
    if(i%2==0):
        l.append(i)         
print(*l)
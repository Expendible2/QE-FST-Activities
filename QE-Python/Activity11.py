d={}
print("How many fruits you need to enter")
n=int(input())
for i in range(n):
    if i in d:
        print("Already Exists")
    else:
        a=input("Enter fruit name")
        b=int(input("Enter price"))
        d[a]=b
opt=input("Enter the value you need to search")
if opt in d:
    print("It is avaliable and price is ",d[opt])
else:
    print("Not available")
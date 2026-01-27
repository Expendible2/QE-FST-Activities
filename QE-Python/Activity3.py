opt1=input("Enter the Value").strip()
opt2=input("Enter the Value").strip()
if(opt1=="rock") and (opt2=="scissors"):
    print("Opt1 wins")
elif(opt1=="rock") and (opt2=="paper"):
    print("Opt2 wins")
elif(opt1=="scissors") and (opt2=="paper"):
    print("Opt1 wins")
elif(opt1=="paper") and (opt2=="rock"):
    print("Opt1 wins")
elif(opt1=="paper") and (opt2=="scissors"):
    print("Opt2 wins")
elif(opt1=="scissors") and (opt2=="rock"):
    print("Opt2 wins")
elif(opt1==opt2):
    print("Draw") 

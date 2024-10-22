temp=int(input("enter the temperature :"))
option=(input("is this celsius or fahrenheit:"))
if (option=="C"):
    f=(9/5*temp)+32
    print(temp,"celsius is",f,"fahrenheit")
elif (option=="F"):
    c=5/9*(temp-32)
    print(temp,"fahrenheit is",c,"celsius")
else:
    print("invalid option")

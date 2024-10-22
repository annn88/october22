number1=int(input("enter first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter third number:"))
if(number1>number2 and number1>number3):
    print("the largest number is number1")
elif(number2>number1 and number2>number3):
    print("the largest number is number2")
else:
    print("the largest number is 3")
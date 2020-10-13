
print("Enter two numbers:-")
x=int(input("FIRST NUMBER:"))
y=int(input("SECOND NUMBER:"))
print("1-ADDITION")
print("2-SUBTRACTION")
print("3-MULTIPLICATION")
print("4-DIVISION")
print("5-MODULUS")
print("ENTER YOUR CHOICE NUMBER FROM THE ABOVE LIST:-")
ch=input("CHOICE NUMBER:")
if (ch=="1"):
    print("ADDITION IS ",x+y)
elif (ch=="2"):
    print("SUBTRACTION IS ",x-y)
elif (ch=="3"):
    print("MULTIPLICTION IS ",x*y)
elif (ch=="4"):
    print("DIVISION IS ",x/y)
elif (ch=="5"):
    print("MODULUS IS ",x%y)
else :
    print("Please Enter valid choice")
     

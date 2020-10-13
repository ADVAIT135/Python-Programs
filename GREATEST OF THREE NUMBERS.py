print("Enter three numbers:-")
x=int(input("First number:"))
y=int(input("Second number:"))
z=int(input("Third number:"))
if x>y and x>z:
    print("first number is greatest:",x)
elif y>z:
    print("seocnd number is greatest:",y)
else:
    print("third number is greatest:",z)
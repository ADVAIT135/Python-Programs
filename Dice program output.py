import random
while (True):
    
    num = random.randint(1,6)
    print(num)
    print("Wanna try again? If Yes enter Y else enter N")
    a=str(input())
    if ((a == 'Y') or (a == 'y')):
        continue
    
    if ((a == 'N') or (a == 'n')):
        print("Hope to see you again. Have a nice day")
        break


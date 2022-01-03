"""NAME : ADVAIT GURUNATH CHAVAN, PRN : 4119008, S.E. ELECTRONICS, SEM 4, TW-6"""
"""Program to find factorial of a number entered through keyboard by applying 
  validation for the user to enter always an integer value(no character or float or string )
 and also for symbols and negative numbers and spaces. Program will reattempt for user input if the
 user enters an invalid number"""
fact_number = 0
flag = True
while flag:
    try:
        fact_number = int(input("Enter the number whose factorial needs to be found : "))
    except ValueError:
        print("Factorial can be found for only integer numbers")
    else:
        if fact_number < 0:
            print("Sorry number can't be a negative number")
        else:
            flag = False

fact_result = 1
i = 1
for i in range(i, fact_number + i):
    fact_result = fact_result * i
print(f"The factorial of the entered number {fact_number} is {fact_result}")

"""NAME : ADVAIT GURUNATH CHAVAN , PRN: 4119008, S.E. ELECTRONICS, SEM IV, TW4"""
"""Program to create 3 lists – a list of names, a list of ages and a list of salaries.
Generate and print a list of tuples containing name, age and salary
from the 3 lists. From this list generate 3 tuples – one containing all
names, another containing all ages and third containing all salaries."""

# creating four list
list_name = ['ADVAIT', 'MARK', 'ELON MUSK']
list_ages = [19, 49, 42]
list_code = [4119008, 12, 16, 78]
list_salary = [900000, 800000, 350000]

# merging the list to create tuples
tuple1 = (list_name[0], list_ages[0], list_code[0], list_salary[0])
tuple2 = (list_name[1], list_ages[1], list_code[1], list_salary[1])
tuple3 = (list_name[2], list_ages[2], list_code[2], list_salary[2])

print("Displaying the merged tuples :-")
print("Details of employee 1 : ", tuple1)
print("Details of employee 2 : ", tuple2)
print("Details of employee 3 : ", tuple3)

# merging the tuples to have name age and salary in separate tuples
tuple_name = (tuple1[0], tuple2[0], tuple3[0])
tuple_ages = (tuple1[1], tuple2[1], tuple3[1])
tuple_code = (tuple1[2], tuple2[2], tuple3[2])
tuple_salary = (tuple1[3], tuple2[3], tuple3[3])
print("Displaying the separated tuples :-")
print("Names of the employees : ", tuple_name)
print("Ages of the employees : ", tuple_ages)
print("Codes of the employees : ", tuple_code)
print("Salaries of the employees : ", tuple_salary)

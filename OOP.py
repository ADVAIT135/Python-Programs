class Student:
    college_name = "MHSSCE"

    def print_name(self,name):
        print("Student name: " + name)

    def print_age(self,age):
        print("Student age: " + age)

    def print_year(self,year):
        print("Year : " + year)
        
    def print_branch(self,branch):
        print("Student branch: " + branch)
        
student_1 = Student()

print(student_1.college_name)

student_1.print_name("Advait")

student_1.print_age(str(18))

student_1.print_year("Second year")

student_1.print_branch("Electronics")

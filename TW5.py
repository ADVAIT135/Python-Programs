"""NAME : ADVAIT GURUNATH CHAVAN, PRN : 4119008, S.E.ELECTRONICS, SEM IV"""
"""If ages of Ram, Shyam, and Ajay are given as an input through the keyboard, write a program to 
determine the youngest of the three.
write a program using object and class"""


class Youngest:  # Creation of class Youngest
    Ram_age = 0
    Shyam_age = 0
    Ajay_age = 0

    def read_age(self):
        self.Ram_age = int(input("Enter the age of Ram in numeric form : "))
        self.Ajay_age = int(input("Enter the age of Ajay in numeric form : "))
        self.Shyam_age = int(input("Enter the age of Shyam in numeric form : "))

    def display_age(self):
        print("Age of Ram entered by you is : ", self.Ram_age)
        print("Age of Shyam entered by you is : ", self.Shyam_age)
        print("Age of Ajay entered by you is : ", self.Ajay_age)

    def validation(self):
        if self.Ram_age <= 0 or self.Ajay_age <= 0 or self.Shyam_age <= 0:
            print("Age must be greater than 0")
            print("The age entered by you for Ram, Shyam or Ajay might be less than 0 or 0")
            print("Please check and run the program again with correct age numbers.")
            print("Exiting the program........")
            exit(0)
        if self.Ram_age > 120 or self.Ajay_age > 120 or self.Shyam_age > 120:
            print("Age cannot be greater than 120. It is impractical(Practically not possible/not possible in reality)")
            print("The age entered by you for Ram, Shyam or Ajay might be greater than 120")
            print("Please check and run the program again with correct age numbers.")
            print("Exiting the program........")
            exit(0)

    def find_youngest(self):
        if self.Ram_age < self.Shyam_age and self.Ram_age < self.Ajay_age:
            print("Ram is the youngest!!")
        elif self.Shyam_age < self.Ajay_age:
            print("Shyam is the youngest!!")
        else:
            print("Ajay is the youngest!!")


y1 = Youngest()  # Creation of object y1
y1.read_age()
y1.display_age()
y1.validation()
y1.find_youngest()

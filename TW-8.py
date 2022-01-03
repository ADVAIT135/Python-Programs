"""NAME : ADVAIT GURUNATH CHAVAN, PRN : 4119008, SEM 4, S.E. ELECTRONICS, TW - 8"""
"""Program to calculate the current age of user by giving his/her date of birth as input"""
import datetime

name = input("Enter your name: ")
print("Hi ", name, " enter your Date of Birth in dd/mm/yyyy format : ")
date_of_birth = input()
day, month, year = [int(x) for x in date_of_birth.split('/')]
date_of_birth_date = datetime.date(year, month, day)
current_date = datetime.date.today()
user_age = current_date - date_of_birth_date
years = user_age.days // 365
days = user_age.days % 365
print("Hi ", name, " you are now ", user_age, " old.")
print(f"OR \nYou are now {years} years and {days} days old.")

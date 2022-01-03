""""Name : ADVAIT GURUNATH CHAVAN ; PRN : 4119008"""
file = open('name_prn.txt', 'w')
file.write("NAME : ADVAIT GURUNATH CHAVAN \n")
file.write("PRN : 4119008")
file.close()
file = open('name_prn.txt', 'r')
for line in file:
    print(line, "\n")
file.close()



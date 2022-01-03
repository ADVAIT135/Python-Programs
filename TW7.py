"""NAME: ADVAIT GURUNATH CHAVAN, PRN : 4119008, S.E.ELECTRONICS, SEM 4, TW-7"""
"""Program to define a function count_lower_upper( )that accepts a string and calculates the number of uppercase and
 lowercase alphabets in it. """


def sorted_user_input(user_input):
    count = {'upper_case': 0, 'lower_case': 0, 'space': 0, 'number': 0, 'symbol': 0}
    for i in user_input:
        if i.isupper():
            count['upper_case'] += 1
        elif i.islower():
            count['lower_case'] += 1
        elif i.isspace():
            count['space'] += 1
        elif i.isnumeric():
            count['number'] += 1
        else:
            count['symbol'] += 1
    print("Input given by user : ", user_input)
    print("Number of characters entered by user : ", len(user_input))
    print("Number of Upper case characters : ", count['upper_case'])
    print("Number of Lower case characters : ", count['lower_case'])
    print("Number of spaces : ", count['space'])
    print("Number of Integer numbers : ", count['number'])
    print("Number of symbols : ", count['symbol'])


string = str(input("Enter any string: "))
sorted_user_input(string)

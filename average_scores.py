"""
Program: average_scores.py
Author: Chadwick Burgett
Last date modified: 06/04/2020

The purpose of this program is to accept any input,
and calculate the average of three test scores
"""

def average(): #This is the function that will accept in user test scores and calculate the average
    tests = 3
    score1 = float(input('Enter your first test score:'))
    score2 = float(input('Enter your second test score:'))
    score3 = float(input('Enter your last test score:'))
    average_tests = (score1 + score2 + score3)/tests
    return average_tests

if __name__ == '__main__':
    first_name = input('Enter your first name:')
    last_name = input('Enter your last name:')
    age = input('Enter your age:')
    age = int(age)
    average_scores = float(average()) #This is the call to the function and assigning it to a variable
    print('%s, %s age: %2d, average grade: %5.2f' %(last_name, first_name, age, average_scores))
    #The above is a formatted print line, each % calls to the end for its data.

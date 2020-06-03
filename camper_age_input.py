"""
Program: camper_age_input.py
Author: Chadwick Burgett
Last date modified: 06/03/2019
The purpose of this program is to take user
input of an age and convert it into months.
"""
def convert_to_months(x):
    """Takes input of years and converts it to months"""
    year = 12
    age = x * year
    return age

if __name__ == '__main__':
    age_in_years = input('Enter an age in years:')
    age_in_months = convert_to_months(int(age_in_years))
    print("The age in months is", age_in_months)
    #print(age_in_months)

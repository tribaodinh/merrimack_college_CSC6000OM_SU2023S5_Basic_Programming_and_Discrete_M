#By Tri Dinh
"""
Asks the user its name, its age, and the current year;
Then, your program should print out a message as:
 -"Dear <name>, you were born either in <year1> or <year2>"
For example, if the user enters: Arnold Schwarzenegger, 75, and 2023, your program should prints out:
  -"Dear Arnold Schwarzenegger, you were born in 1947 or 1948
"""

def birth_year():
    name = input("what is your name: ")
    age = int(input("what is your age: "))
    current_year = int(input("what is the current year: "))

    year1 = current_year - age
    year2 = current_year - age - 1

    print("Dear " + name + ", you were born either in " + str(year2) +" or " + str(year1))

birth_year()

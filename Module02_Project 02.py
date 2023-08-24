#by Tri Dinh

"""
Asks the user a number as a string (to set a maximum number of digits in your program is ok);

○ Your program should ask which is the base (an Integer from 2 to 16);

○ With that information, your program should compute the binary and decimal representations of the number, then print it out as a string

○ For example, if the user enters: FA and 16, your program should print out:

-- "FA in base 16 is: 250 in base 10 and 11111010 in base 2"

○ If the user enters: 34 and 5, your program should print:

-- "34 in base 5 is: 19 in base 10 and 10011 in base 2"
"""
string = input("please enter a number: ")
base = int(input("please enter a base: "))

def decimal_conversion_to_binary(num):
    string = bin(num)
    return string[2:]

def conversion_to_decimal(num, exp, base):
    
    numbers_conversion = {
        "0": (0 * base**exp),
        "1": (1 * base**exp),
        "2": (2 * base**exp),
        "3": (3 * base**exp),
        "4": (4 * base**exp),
        "5": (5 * base**exp),
        "6": (6 * base**exp),
        "7": (7 * base**exp),
        "8": (8 * base**exp),
        "9": (9 * base**exp),
        "a": (10 * base**exp),
        "A": (10 * base**exp),
        "b": (11 * base**exp),
        "B": (11 * base**exp),
        "c": (12 * base**exp),
        "C": (12 * base**exp),
        "d": (13 * base**exp),
        "D": (13 * base**exp),
        "e": (14 * base**exp),
        "E": (14 * base**exp),
        "f": (15 * base**exp),
        "F": (15 * base**exp),
    }
    return numbers_conversion.get(num, "nothing")

lis = []
lis.extend(string)

binary = ""
decimal = 0

for index, letter in enumerate(lis):
   decimal += conversion_to_decimal(letter, (len(lis) - 1) - index, base)
   
binary = decimal_conversion_to_binary(decimal)

print(f"{string} in base {base} is: {decimal} in base 10 and {binary} in base 2")
    



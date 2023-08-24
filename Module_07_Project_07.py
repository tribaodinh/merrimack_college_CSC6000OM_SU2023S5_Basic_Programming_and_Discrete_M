#Tri Dinh
"""
Write a Python program that receives information about a lottery game based on the player guessing k numbers out of n possible numbers. Assume that the game consists of the players betting on k numbers, the lottery agent randomly draws k numbers, and the player wins big if hitting all k drawn numbers, and wins little if hitting k-1 drawn numbers.

● Your program should ask the users the values of n and k;

    ○ Then your program should compute:

        ● the probability of winning big (hitting all k drawn numbers) and

        ● the probability of winning little (hitting k-1 drawn numbers).
"""
import math
def prob(n, k):
    denominator = 1
    numerator = 1
    numerator_2nd = 1
    for x in range(n, n-k, -1):
        denominator *= x
    
    for i in range(2, k+1):
        numerator *=i
    for i in range(2, k):
        numerator_2nd *=i
    
    intc = numerator/numerator_2nd
    x, y = simplify_fraction(numerator, denominator, intc)
    return x, y

def simplify_fraction(numerator, denominator, numerator2):
    if math.gcd(numerator, denominator) == denominator:
        return int(numerator/denominator), int(numerator2/denominator)
    elif math.gcd(numerator, denominator) == 1:
        return str(numerator) + "/" + str(denominator), str(numerator2) + "/" + str(denominator)
    else:
        top = numerator / math.gcd(numerator, denominator)
        bottom = denominator / math.gcd(numerator, denominator)
        return str(top) + "/" + str(bottom), str(numerator2) + "/" + str(bottom)


n, k = [int(x) for x in input("Enter the amount of n  numbers there are in the lottery and enter the k numbers you want to bet on, respectably (seperated by a space like \"10 5\"): ").split()]

A, B = prob(n,k)

print(f"There is a {A} chance to win big if you draw all {k} numbers")
print(f"There is a {B} chance to win very little if you draw just {k-1} numbers")



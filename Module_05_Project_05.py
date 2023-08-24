#Tri Dinh
"""
Write a Python program to print a Pascal's Triangle.

○ Your program should ask the user the number of lines (use a limit from 4 to 8 lines) of the Pascal's Triangle.

○ Your program should have a function that computes the binomial coefficient of n and k, and this function should be used to find the values of the cells of the Pascal's Triangle.

○ The great challenge of this program is the output formatting which requires you to assemble the lines with the proper space.
"""
#ask the user the number of lines (use a limit from 4 to 8 lines) of the Pascal's Triangle
def Pascal_Triangle(x):
    for n in range(x):
        for k in range(n+1):
            answer = comb(k,n)
            if k == 0:
                print(f"{answer: >{25 - (2*n)}}", end = "")
            else:
                print(f"{answer: >4}", end = "") 
        print("\n")

def comb(k,n):
    ans = 1
    if (k > n//2):
        k = n-k
    for i in range(k):
        ans *= (n-i) / (i+1)
    return int(ans)

#ask the user the number of lines (use a limit from 4 to 8 lines) of the Pascal's Triangle
lines = int(input("how many line do you want in the Pascal's Triangle (between 4 to 8): "))
while(lines < 4 or lines > 8):
    lines = int(input("Please enter a number between 4 to 8: "))

Pascal_Triangle(lines)

#by tri dinh
"""
○ Asks the user a scale factor a and a common ratio r;

○ Your program inform the user if the GP informed converges to a sum regardless of its number of elements:

    ■ If the GP converges to a sum regardless of the number of elements, your program should compute the sum of infinite elements;

    ■ Otherwise, your program should ask the number of elements n, and compute the sum of all elements;

○ With that information, your program should print out the first 3 elements of the GP and the computed sum.

For example, if the user enters: a = 10 and r = 0.5, your program should output:

    -This GP converges with infinite elements to 20

    -For example, if the user enters: a = 10 and r = -0.5, your program should output:

        -This GP converges with infinite elements to 6.6666667

    -For example, if the user enters: a = 1 and r = 2, your program should output:

        -This GP does not converge to a finite number with infinite elements and ask for n, and if the user enters n = 10, the final output should be:

        -This GP sum with 10 elements is equal to 1023
"""
#your program should print out the first 3 elements of the GP and the computed sum.
def GP_sum(a, r):
    #for -1 < r < 1
    if (-1 < r < 1):
        print("the first 3 numbers of the sequence are ", end = " ")
        for number in range(1,4):
            print(a * (r ** number-1)/ (r - 1), end=", ")
        print("...")
        print("This GP converges with infinite elements to", a / (1 - r))
    #for r = 1
    elif (r == 1):
        n1 = int(input("This GP does not converge to a finite number with infinite elements so enter a specific number of elements: "))
        print("since common_factor is equal to 1 then the sequence will be just ")
        for n in range(1,4):
            print(a* r ** (n-1), end=", ")
        print("...")

        print(f"This GP sum with {n1} elements is equal to to {a * n1}")
    
    #for r = -1
    elif (r == -1):
        n2 = int(input("This GP does not converge to a finite number with infinite elements so enter a specific number of elements: "))
        print("since common_factor is equal to -1 then the sequence will be just ")
        
        #even number of elements 
        if (n2 % 2 == 0):
            for n in range(1,4):
                print(a* r ** (n-1), end=", ")
            print("...")
            print(f"This GP sum with {n2} elements is equal to {a}")

        #odd number of elements 
        if (n2 % 2 == 1):
            for n in range(1,4):
                print(a* r ** (n-1), end=", ")
            print(f"This GP sum with {n2} elements is equal to {0}")

    #Otherwise, your program should ask the number of elements n, and compute the sum of all elements
    else:
        n3 = int(input("This GP does not converge to a finite number with infinite elements so enter a specific number of elements: "))
        if n3 <= 3:
            print("The sequence is ", end=" ")
            for n in range(1,n3 +1):
                print(a* r ** (n-1), end = " ")
                if n == n3:
                    break
                print(", ", end="")

        else:
            print("the first 3 numbers of the sequence are ", end="")
            for n in range(1,4):
                print(a* r ** (n-1), end=", ")
            print("...", end = "")
        print(f"\nThis GP sum with {n3} elements is equal to {a * (r ** n3-1)/ (r - 1)}")

# Asks the user a scale factor a and a common ratio r
scale_factor = float(input("enter a scale factor: "))
common_factor = float(input("enter a common_factor: "))

GP_sum(scale_factor, common_factor)
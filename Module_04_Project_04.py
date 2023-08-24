#Tri Dinh
"""
Write a Python program to compute Arrangements of Multisets that:

○ Asks the user a number of subsets (no smaller than 3, no greater than 8);

    ■ j

○ Asks the user the size of each subset (from 1 to 5);

    ■ m_i with i going from 1 to j

○ Asks the user the total number of the arrangement (a number smaller than the sum of sizes of the subsets - n)

    ■ k

○ Then, it computes and prints the number of arrangements of k elements out of n, considering the subsets of size mi
"""
def permutation(n):
    acc = 1
    for i in range(2, n+1):
        acc *=i
    return acc

def arrangement_of_multiset(m, k, n):
    
    numerator = permutation(n)
    n_k = permutation(n-k)
    m_total = 1
    for i in m:
        m_total *= permutation(i)
    
    denomiator = n_k * m_total
    print(f"the number of arrangements of {k} elements out of {n} is {numerator/denomiator}")

#Asks the user a number of subsets (no smaller than 3, no greater than 8)
j = int(input("enter a number of subsets (between 3 and 8): "))
while (3 > j or j > 8 ):
    j = int(input("enter a number between 3 and 8: "))

#Asks the user the size of each subset (from 1 to 5)
m_list = []
for i in range (1, j+1):
    m = int(input("enter the size of subsets (between 1 and 5): "))
    while (1 > m or m > 5):
        m = int(input("Please enter a number between 1 and 5: "))
    m_list.append(m)


n = sum(m_list)
#Asks the user the total number of the arrangement (a number smaller than the sum of sizes of the subsets
k = int(input(f"enter a number less than {n}: "))
while (k > n):
    k = int(input(f"enter a number less than {n}: "))

arrangement_of_multiset(m_list, k, n)

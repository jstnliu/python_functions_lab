# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# For example:
#  sum_to(6)  # returns 21
#  sum_to(10) # returns 55

def sum_to(n):
    total = 0 
    for i in range(1, n + 1):
        total += i 
    return total 


# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# For example:
#  largest([1, 2, 3, 4, 0])  # returns 4
#  largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(list):
    largest_num = 0
    for n in list:
        if n > largest_num:
            largest_num = n
    return largest_num 


# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

# For example:
#  occurrences('fleep floop', 'e')   # returns 2
#  occurrences('fleep floop', 'p')   # returns 2
#  occurrences('fleep floop', 'ee')  # returns 1
#  occurrences('fleep floop', 'fe')  # returns 0

def occurrences(str1, str2):
    count = 0
    start = 0
    while start < len(str1):
        idx = str1.find(str2, start)
        if idx != -1:
            count += 1
            start = idx + 1
        else: 
            break
    return count


# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

# For example:
#  product(-1, 4) # returns -4
#  product(2, 5, 5) # returns 50
#  product(4, 0.5, 5) # returns 10.0

def product(*args):
    n = 1
    for arg in args:
        n *= arg
    return n


# -----------------------------------
# BONUS CHALLENGE
# Write a function named steps_to_zero that accepts a non-negative integer as an argument, 
# and returns the number of steps it took to reduce the integer to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# For example:
#  steps_to_zero(14) # returns 6
# Explanation:

#  Step 1) 14 is even; divide by 2 and obtain 7. 
#  Step 2) 7 is odd; subtract 1 and obtain 6.
#  Step 3) 6 is even; divide by 2 and obtain 3. 
#  Step 4) 3 is odd; subtract 1 and obtain 2. 
#  Step 5) 2 is even; divide by 2 and obtain 1. 
#  Step 6) 1 is odd; subtract 1 and obtain 0.

def steps_to_zero(num):
    steps = 0
    integer = int(num)
    while integer > 0:
        if integer % 2 == 0:
            integer /= 2
        else:
            integer -= 1 
        steps += 1
    return steps

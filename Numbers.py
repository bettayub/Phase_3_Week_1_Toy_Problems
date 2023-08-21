def two_positive_numbers(a, b, c): #defining a function
    positives = [num for num in (a, b, c) if num > 0]
    return len(positives) == 2


#test cases for this code
print(two_positive_numbers(2, 4, -3))  # True
print(two_positive_numbers(-4, 6, 8))  # True
print(two_positive_numbers(4, -6, 9))  # True
print(two_positive_numbers(-4, 6, 0))  # False
print(two_positive_numbers(4, 6, 10))  # False
print(two_positive_numbers(-14, -3, -4))  # False

#how to run
#python3 Numbers.py


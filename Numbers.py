def exactly_two_positive(a, b, c):
    positives = [num for num in (a, b, c) if num > 0]
    return len(positives) == 2

print(exactly_two_positive(2, 4, -3))  # True
print(exactly_two_positive(-4, 6, 8))  # True
print(exactly_two_positive(4, -6, 9))  # True
print(exactly_two_positive(-4, 6, 0))  # False
print(exactly_two_positive(4, 6, 10))  # False
print(exactly_two_positive(-14, -3, -4))  # False

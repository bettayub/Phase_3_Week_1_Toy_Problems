def exactly_two_positive(a, b, c):
    positives = [num for num in (a, b, c) if num > 0]
    return len(positives) == 2

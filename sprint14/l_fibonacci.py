def fibonacci(count, length):
    base = 10 ** length
    ab = [1, 1]
    for i in range(count-1):
        sum = (ab[0] + ab[1]) % base
        ab[0] = ab[1]
        ab[1] = sum
    return ab[1]
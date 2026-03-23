def power(base, exponent):
    if base <= 0 or exponent < 0:
        return 0
    elif exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

def sum(num):
    if num <= 0:
        return 0
    else:
        return num + sum(num - 1)

def displaySequence(start, difference, numOfTerms):
    if numOfTerms <= 0:
        print()
    else:
        numOfTerms -= 1
        print(start, end = " ")
        displaySequence(start + difference, difference, numOfTerms)

def sumTheDigits(num):
    if num < 0:
        return 0
    elif num < 10:
        return num
    else:
        return num % 10 + sumTheDigits(num // 10)
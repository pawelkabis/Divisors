divisors = int(input('Enter number: '))
listRange = range(1, divisors+1)

for element in listRange:
    if divisors%element == 0:
        print(element, end=", ")
numbers = input()

numbers = numbers.strip().split(" ")

impact_factor = int(numbers[1])

articles = int(numbers[0])

scientists = (articles*(impact_factor-1)) + 1

print(scientists)

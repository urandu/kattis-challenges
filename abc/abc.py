numbers = input()
order = input()

numbers = numbers.strip().split(" ")
print(numbers)
numbers.sort()
print(numbers)
order = list(order.strip())
number_dict = {
    "A": numbers[0],
    "B": numbers[1],
    "C": numbers[2]
}
output = ""
for item in order:
    output = output+number_dict[item]+" "

print(str(output.strip()))

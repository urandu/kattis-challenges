valid_set = [1, 1, 2, 2, 2, 8]
input = input()

input = input.strip().split(" ")

test_set = list(map(int, input))
output = ""
for i in range(6):
    output = output+" " + str(valid_set[i] - test_set[i])

print(output.strip())

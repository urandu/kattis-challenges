import re
input = input()

output = re.sub('[^A-Z]', '', input)

print(output)

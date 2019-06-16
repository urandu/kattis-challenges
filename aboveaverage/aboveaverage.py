classes = input()
output1 = []
for i in range(int(classes)):
    class_data = input()
    marks = class_data.split(" ")
    y = 0
    total_students = int(marks[0])
    marks.pop(0)
    marks = list(map(int, marks))
    average = sum(marks)/float(len(marks))
    for x in marks:
        x = int(x)
        if x > average:
            y = y+1
    output = (y/float(total_students))*100.000
    output1.append(format(output, ".3f"))
for t in output1:
    print("{}%".format(t))



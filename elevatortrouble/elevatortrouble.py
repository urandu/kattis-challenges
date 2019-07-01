inputs = input().strip().split(" ")


no_of_states = int(inputs[0])

# no_of_states = list(range(1, no_of_states+1))
start = int(inputs[1])
goal = int(inputs[2])
steps_right = int(inputs[3])
steps_left = int(inputs[4])
es = 0
x = 0
steps = 0
while start != goal and es == 0:

    if start < goal:
        # if x ==1:

        distance = goal - start
        if steps_right == 0:
            es = 1
        else:
            mod_distance = distance % steps_right

            if mod_distance == 0:
                steps = steps + (distance/steps_right)
                start = goal
            elif mod_distance == distance:
                if (start + steps_right) > no_of_states:
                    if start <= steps_left:
                        es = 1
                    else:
                        start = start - steps_left
                        steps = steps + 1
                else:
                    start = start + steps_right
                    steps = steps + 1
            else:
                steps = steps + ((distance-mod_distance)/steps_right)
                start = steps*steps_right + start
                if start > no_of_states:
                    if start <= steps_left:
                        es = 1
                    else:
                        start = start - steps_left
                        steps = steps + 1
    else:
        goal, start = start, goal
        steps_right, steps_left = steps_left, steps_right
        x = 1


if es == 1:
    print("use the stairs")
else:
    print(int(steps))



no_of_states = list(range(1, 11))
goal = 1

start = 5

steps_right = 1
steps_left = 1
es = 0
print(no_of_states)
# exit()
steps = 0
while start != goal and es == 0:
    if start < goal:
        distance = goal - start
        mod_distance = distance % steps_right

        if mod_distance == 0:
            steps = steps + (distance/steps_right)
            start = goal
        else:
            steps = (distance-mod_distance)/steps_right
            start = goal - mod_distance
            if mod_distance == distance:
                es = 1
    else:




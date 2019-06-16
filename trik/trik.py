cups = input()

order = list(cups.strip())

ball = 1

for a in order:
    if ball == 1 and a == "A":
        ball = 2
    elif ball == 2 and a == "A":
        ball = 1
    elif ball == 2 and a == "B":
        ball = 3
    elif ball == 3 and a == "B":
        ball = 2
    elif ball == 1 and a == "C":
        ball = 3
    elif ball == 3 and a == "C":
        ball = 1

print(ball)

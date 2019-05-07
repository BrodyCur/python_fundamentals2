runner1 = input("Runner 1 name?: ")
runner2 = input("Runner 2 name?: ")
runner3 = input("Runner 3 name?: ")

def runner_speed(runner):
    distance = float(input(f"How far did {runner} run?"))
    mins = float(input(f"How long did it take in mins?"))

    secs = mins * 60
    return distance / secs

speed1 = runner_speed(runner1)
speed2 = runner_speed(runner2)
speed3 = runner_speed(runner3)

def determine_winner():
    if speed1 > speed2 and speed1 > speed3:
        print("{} was the fastest at {} m/s".format(runner1, speed1))
    elif speed2 > speed1 and speed2 > speed3:
        print("{} was the fastest at {} m/s".format(runner2, speed2))
    elif speed3 > speed1 and speed3 > speed2:
        print("{} was the fastest at {} m/s".format(runner3, speed3))
    elif speed1 == speed2 and speed2 == speed3:
        print("Everyone tied at {} m/s".format(speed1))
    else:
        print("Well done everyone!")

determine_winner()
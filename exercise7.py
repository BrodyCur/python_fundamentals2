def runner_data(id):
    distance = float(input(f"How far did runner {id} run?\n"))
    mins = float(input(f"How long did it take in mins?\n"))

    secs = mins * 60
    return distance / secs

speed1 = runner_data(1)
speed2 = runner_data(2)
speed3 = runner_data(3)

def determine_winner():
    if speed1 > speed2 and speed1 > speed3:
        print(f"Person 1 was the fastest at {speed1} m/s")
    elif speed2 > speed1 and speed2 > speed3:
        print(f"Person 2 was the fastest at {speed2} m/s")
    elif speed3 > speed1 and speed3 > speed2:
        print(f"Person 3 was the fastest at {speed3} m/s")
    elif speed1 == speed2 and speed2 == speed3:
        print(f"Everyone tied at {speed1} m/s")
    else:
        print("Well done everyone!")

determine_winner()
# runner1 = input("Runner 1 name?: ")
# runner2 = input("Runner 2 name?: ")
# runner3 = input("Runner 3 name?: ")

def collect_data(runner_id):
    name = input(f"Runner {runner_id} name?: ")
    distance = float(input(f"How far did {name} run? "))
    mins = float(input(f"How long did it take in mins? "))

    return {
        "id": runner_id,
        "name": name,
        "speed": distance / (mins * 60)
    }

results = []

for id in [1,2,3]:
    runner_info = collect_data(id)
    results.append(runner_info)

# TODO: Sorts the array of dictionaries by key

for runner in results:
    # print(runner)
    print(f"{runner['name']} ran at {runner['speed']} m/s")


# def determine_winner():
#     if (speed1 > speed2) and (speed1 > speed3):
#         print(f"{1} was the fastest at {speed1} m/s")

#     elif speed2 > speed1 and speed2 > speed3:
#         print(f"{2} was the fastest at {speed2} m/s")

#     elif speed3 > speed1 and speed3 > speed2:
#         print(f"{3} was the fastest at {speed3} m/s")

#     elif speed1 == speed2 and speed2 == speed3:
#         print(f"Everyone tied at {speed1} m/s")
        
#     else:
#         print("Well done everyone!")

# determine_winner()
print("Hey, do you know the temperature in Farenheit?")
user_temp = int(input())

def celcius_conversion(farenheit):
    celcius = (farenheit - 32) * 5/9
    return celcius

print(f"Wow that's {celcius_conversion(user_temp):0.1f} in Celcius!")
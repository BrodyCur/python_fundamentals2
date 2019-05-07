def string(word):
    if len(word) < 8:
        return False
    else:
        return True

print(string('Brody'))
print(string('BrodyCurrie'))
print(string('Bitmaker Rocks!'))
print(string('I like to code'))
print(string('python'))
print(string('dang'))
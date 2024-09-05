oldlist = [1, 2, 3]

newlist = [x for x in oldlist if x > 1]

print(newlist)

def add_10(inputnumber):
    return inputnumber + 10

newerlist = [add_10(x) for x in oldlist]

print(newerlist)
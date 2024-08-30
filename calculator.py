def adder(operator1, operator2): return operator1 + operator2

def subtractor(operator1, operator2): return operator1 - operator2

def multiplier(operator1, operator2): return operator1 * operator2

def divider(operator1, operator2): return operator1 / operator2

operation = int(input("Select operation: 1=+ 2=- 3=* 4=/"))
operator1 = float(input("Enter the first number: "))
operator2 = float(input("Enter the second number: "))

result = None

if operation == 1: result = adder(operator1, operator2)
if operation == 2: result = subtractor(operator1, operator2)
if operation == 3: result = multiplier(operator1, operator2)
if operation == 4: result = divider(operator1, operator2)

print(result)
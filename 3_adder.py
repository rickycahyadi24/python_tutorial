import math
sum = 0
while True:
    x1 = input ("Enter x1: ")
    x2 = input ("Enter x2: ")
    x3 = input ("Enter x3: ")
    op = input("Enter operator: ")
    if op == "+":
        sum = int(x1) + int(x2)
    elif op == "-":
        sum = int(x1) - int(x2)
    elif op == "*":
        sum = int(x1) * int(x2)
    elif op == "/":
        sum = int(x1) / int(x2)
    elif op == "avg":
        sum = (int(x1) + int(x2))/2
    elif op == "SD":
        mean = (int(x1) + int(x2) + int(x3))/3
        step1 = int(x1) - mean
        step2 = int(x2) - mean
        step3 = int(x3) - mean
        step4 = (step1)**2 + (step2)**2 + (step3)**2
        sum = math.sqrt(step4/3)
    
    print(f"Sum: {sum}")
    res = input("Continue? (Y/N)")
    if res == "N":
        break;
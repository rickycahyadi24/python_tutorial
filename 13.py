import statistics, math

def my_sd(input):
    print(f'Input : {input}')
    length = len(input)
    sum = 0
    mean = statistics.mean(input)
    print(f'Mean  : {mean}')
    for x in input:
        sum += (int(x) - mean)**2
    sum = sum / length
    output = math.sqrt(sum)    
    return output

# 1. Input
input = [20,23,18]

# 2. Process
answer = my_sd(input)

# 3. Output
print(f'Answer: {answer}')
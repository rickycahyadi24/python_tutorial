#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    cov = 0 
    print(f'Input x= {input_x},', f'Input y= {input_y}')
    n=len(input_x)
    meanx=statistics.mean(input_x)
    meany=statistics.mean(input_y)
    print(f'Mean x= {meanx},', f'Mean y= {meany}')
    for a in range(len(input_x)):
        cov += (input_x[a]-meanx)*(input_y[a]-meany)
    cov=cov/n
    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Answer: {answer}')

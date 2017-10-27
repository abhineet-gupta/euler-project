#p25
#The 12th term, F12, is the first term to contain three digits.
#What is the first term in the Fibonacci sequence to contain 1000 digits?

import time

def num_digits(num):
    count = 0
    while num != 0:
        num = num//(10)
        count += 1
    return count

fs = [1, 1]

max_digits = 1000
i = 3

start_time = time.time()
while (num_digits(fs[1]) < max_digits):
    temp = fs[0] + fs[1]
    fs.append(temp)
    fs.pop(0)
    i += 1

print (i-1, fs[1])

print (time.time() - start_time, "seconds")

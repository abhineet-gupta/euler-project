##For a positive integer n and digits d, we define F(n, d) as the number of the divisors of n whose last digits equal d.
##For example, F(84, 4) = 3. Among the divisors of 84 (1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84), three of them (4, 14, 84) have the last digit 4.
##
##We can also verify that F(12!, 12) = 11 and F(50!, 123) = 17888.
##
##Find F(106!, 65432) modulo (1016 + 61).

def fact(x):
    if x==1:
        return 1
    else:
        return x * fact(x-1)

def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num%2 or not num%3:
        return False
    for i in range(5, int(num**0.5) + 1, 6):   
        if not num%i or not num%(i + 2):
            return False
    return True

def num_digits(num):
    count = 0
    while num != 0:
        num = num//(10)
        count += 1
    return count

def F(num, digit):
    result = []
    if num == 1:
        return result
    if digit == 1:
        result = [1]
    div = 10 ** num_digits(digit)
    
    flag = True
    i = 2
    min = 0
    
    if not is_prime(num):
        while (flag):
            if num%i == 0:
                min = i
                flag = False
                if i % div == digit:
                    result.append(i)
            i += 1
                
        for j in range(i, num//(min) + 1):
            if not num%j:
                if j % div == digit:
                    result.append(j)

    if num % div == digit:
        result.append(num)
    return result

import math

print (len((F(math.factorial(50), 123))))

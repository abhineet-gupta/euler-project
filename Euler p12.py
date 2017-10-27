#p12
#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?

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

def divisors(num):
    if num == 1:
        return []
    result = [1]
    flag = True
    i = 2
    min = 0
    
    if not is_prime(num):
        while (flag):
            if num%i == 0:
                min = i
                flag = False
                result.append(i)
            i += 1
                
        for j in range(i, num//(min) + 1):
            if not num%j:
                result.append(j)
    result.append(num)                        
    return result

max_divisors = 500
max_num = 2000
max_len = 1

tn = 3
i = 2

#while (len(divisors(tn)) < max_divisors):
while (i < max_num):
    i += 1
    tn = tn + i
    
    if len(divisors(tn)) > max_len:
        print (i, len(divisors(tn)), tn)
        max_len = len(divisors(tn))

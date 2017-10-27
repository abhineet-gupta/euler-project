#p21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
#and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
#therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

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
    result = [1]
    if num == 1:
        return result
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
                        
    return result

def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum

def d(n):
    if n == 1:
        return 0
    list = divisors(n)
    return sum_list(list)

def has_amicable_pair(a):
    b = d(a)
    if a != b and b != 1:
        if d(b) == a:
            return True
    return False

##print (is_prime(13))
##print (divisors(220))
##print (sum_list([1, 3, 5, 5]))
##print (d(220))
##print (has_amicable_pair(220))

max = 10000
sum = 0
ap = []
a = 0
b = 0

for i in range(6, max):
    if i not in ap:
        a = d(i)
        b = d(a)
        if i != a:
            if i == b:
                ap.append(i)
                ap.append(a)
            
    i += 1

sum = sum_list(ap)
print (sum)

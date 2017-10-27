#p3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#
============================================
##
##def is_prime(n):
##    for i in range(2, n//2):
##        if i%2 != 0:
##            if n%i==0:
##                return False
##    return True

###num = 600851475143
##num = 13195
##
##for i in range(2, (num//2)+1):
##    if i%2 != 0:
##        if num%i==0:
##            if is_prime(i):
##                max_pf = i
##            
##print (max_pf)


#==========Trial Division - WORKS!=============
num = 600851475143
count = 2

def factorise():
    global count, num
    if num%count != 0:
        count += 1
    else:
        num = num // count

while (count * count <= num):
    factorise()

print (num)

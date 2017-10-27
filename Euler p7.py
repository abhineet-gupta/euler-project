#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6th prime is 13.
#What is the 10 001st prime number?

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

i = 3
num = 5

max = 10001

while (i <= max):
    if is_prime(num):
        i += 1
    num += 2

print (i-1, num-2)

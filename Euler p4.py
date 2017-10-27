#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    num_d = []
    
    while num != 0:
        num_d.append(num%10)
        num = num // 10
    
    num_d.reverse()
    #print num_d
    
    for i in range(len(num_d)):
        if num_d[i] != num_d[-i-1]:
            #print num_d[i], num_d[-i-1]
            return False
    return True
    
max_pal = 100

num1 = range(100, 1000)
num2 = range(100, 1000)

for n1 in num1:
    for n2 in num2:
        if is_palindrome(n1*n2):
            if max_pal < n1*n2:
                max_pal = n1*n2

print (max_pal)

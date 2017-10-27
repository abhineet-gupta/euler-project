#p48
#The series, 1^1 + 22 + 33 + ... + 1010 = 10405071317.
#Find the last ten digits of the series, 1^1 + 22 + 33 + ... + 10001000.

max = 1000
sum = 0
i = 1

while i <= max:
    sum += (i**i)
    i += 1
    
print (sum)

##p5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

list = [11, 13, 14, 16, 17, 18, 19, 20]
#list = [7, 8, 9, 10]
flag = 0

i = 11

while (flag < len(list)):
    flag = 0
    for j in list:
        if i%j==0:
            flag += 1
    i += 1
    
print (i-1)


#==================POSSIBLY FASTER VERSION BELOW========
###2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
###What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
##
##
##def lcm(list):
##    flag = 0
##    i = list[-1]
##    while (flag < len(list)):
##        flag = 0
##        for j in list:
##            if i%j==0:
##                flag += 1
##        i += 1
##    return i-1
##
##
##listb = [20, 19, 18, 17, 16, 14, 13, 11]
###listb = [10, 9, 8, 7]
##
###print (lcm(listb))
##temp = 10
##
##for i in range(len(listb)-1):
##    temp = lcm([temp, listb[i+1]])
##    
##print (temp)

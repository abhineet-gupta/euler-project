#p11
#What is the greatest product of four adjacent numbers in the same direction 
#(up, down, left, right, or diagonally) in the 20×20 grid?

file = open('p11.txt')
lines = file.readlines()

list = []
for line in lines:
    list.append([int(i) for i in line.split()])
    
sum = 0
for i in range (len(list)):
    for j in range (len(list[i])):
        sum += list[i][j]
print (sum)


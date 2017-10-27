#p22
##Using names.txt, a 46K text file containing over five-thousand first names,
##begin by sorting it into alphabetical order.
##Then working out the alphabetical value for each name,
##multiply this value by its alphabetical position in the list
##to obtain a name score.
##
##For example, when the list is sorted into alphabetical order,
##COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
##is the 938th name in the list.
##So, COLIN would obtain a score of 938 × 53 = 49714.
##
##What is the total of all the name scores in the file?



with open('names.txt') as name_file:
    names = name_file.read().replace('"', '').split(',')

names.sort()

score = 0
for name in names:
    alpha_value = 0
    for letter in name:
        alpha_value += (ord(letter) - 64)
    score += (alpha_value * (names.index(name)+1))

print (score)

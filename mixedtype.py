myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
     print("{} is of the data type {}".format(item,type(item)))

# Program to find the sum of all numbers stored in a list
#list of numbers
myList=[9,8,56,90,78]

sum=0
for val in myList:
    sum= sum+val
    print(sum)
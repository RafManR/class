#N2
#Concatenate two lists index-wise.
#Input:

#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#Output:

#['My', 'name', 'is', 'Kelly']

#N1

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(list1[0] + list2[0] + list1[1] + list2[1] + list1[2] + list2[2] + list1[3] + list2[3])


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
for i in range(len(list1)):
    list1[i] += list2[i]
print(list1)

#N2
#Python's zip() function is defined as zip(*iterables).
# The function takes in iterables as arguments and returns an iterator.
# #This iterator generates a series of tuples containing elements from each iterable.
# #zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=list((zip(list1, list2)))

x=[]
for i in list3:
    x.append(''.join(i))
print(x)

#N3
list1 = ["M", "na", "i", "Ke", "0"]
list2 = ["y", "me", "s", "lly"]
list3 = []

def sum_list(list1=[], list2=[]) :
    for i in range(0, len(list2), 1) :
        list3.append(list1[i] + list2[i])
    print(list3)

sum_list(list1,list2)

#N3
#Given a Python list of numbers. Turn every item of a list into its square

#N1

start_list = [6, 4, 8, 22]
for i in range(len(start_list)):
    start_list[i] *= start_list[i]
print(start_list)

#N4
#Write a program that will calculate sum of lists members.
#N1
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))


#N5
#

#N1

s = [1,2,3,4,5,2,5,6,7,1,3,9,3,5]
x=[]

[x.append(i) for i in s if i not in x]
print(x)

#N2

test_list = ["a", "a", "b", "b", "h", "h", "r", "r",]

res_list = []

for i in range(len(test_list)):

    if test_list[i] not in test_list[i + 1:]:

        res_list.append(test_list[i])

print(res_list)


#N6
#Write a Python program to get unique values from a list.

#N1


numbers = [2, 3, 3, 4, 2,]

def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(get_unique_numbers(numbers))

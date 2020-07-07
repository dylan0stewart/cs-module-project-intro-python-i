# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
for num in y:
    x.append(num)
# x.append(y) <-- easy way, but it doesnt quite work how the assignment asked
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
for num in x:
    if num == 8:
        x.remove(num)
    else:
        pass
#x.remove(8) <-- this way works and is easier, but i wanted to think of a more generalized way to do it
print(x)


# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.remove(10)
x.append(99)
x.append(10)
print(x) #<-- i know theres a better way, hopefully I'll have time to come back to it


# Print the length of list x
print(len(x))


# Print all the values in x multiplied by 1000
new_list = []
for num in x:
    new_list.append(num*1000)
print(new_list)

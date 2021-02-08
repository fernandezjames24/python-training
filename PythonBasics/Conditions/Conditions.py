

# changed integer variable number to 16 from 10 to fulfill condition #1
number = 19

# changed second_number to 'not 11' to become False so if second_number
# is on the condition phase 
# it will invert False to True since 'not' operator is an inverter. This will fulfill
# condition #6
second_number = not 11


# on this case, we will put any amount of element/s inside list. Since the condition
# is to "change the variables", we will change it to a list with element/s instead
# of appending an element to it. This will fulfill condition #2
first_array = [1, "James", "Patrick"]



# we will reduce the element of second_array list to 2 elements to fulfill condition
# #3
second_array = [1,2]

#condition #1 said number is greater than 15 but number is 16 so it will print
# "1"
if number > 15:
    print("1")

#condition #2 statement means first_array list must have an element to become True.
# we changed first_array from empty list to a 
if first_array:
    print("2")

# condition #3 states that second_array list length (amount of elements) must 2
# to become True
if len(second_array) == 2:
    print("3")

# condition #4 states that the sum of lengths of 2 list first_array and second_array
# must be 5
if len(first_array) + len(second_array) == 5:
    print("4")

# condition #5 states that first_array list must have an element and its first index value
# is 1
if first_array and first_array[0] == 1:
    print("5")

# since second_number is False due to its value inverted, condition #6 inverts it again;
# becomes True
if not second_number:
    print("6")

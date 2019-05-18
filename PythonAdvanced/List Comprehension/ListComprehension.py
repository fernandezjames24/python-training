numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

# exclude negative numbers and put it on newlist variable
newlist = [x for x in numbers if x > 0]
print(newlist)

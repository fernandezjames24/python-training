x = object()
y = object()


#codes...

#creating variable x_list and y_list which contains 10 instances of x and y
#respectively

x_list = [x] * 10
y_list = [y] * 10

#creating variable big_list which contains the concatenation of
#x_list and y_list

big_list = x_list + y_list


#print output
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))


#testing

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


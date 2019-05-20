from functools import partial

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x


mypartial = partial(func,5,4,3)

print(mypartial(22))


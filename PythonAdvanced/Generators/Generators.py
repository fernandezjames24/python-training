# Fibonacci function that returns an iterable
def fib():
    a = 0
    b = 1
    for x in range(100):
        
        a,b = b, a+b
        yield a
    

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10: 
            break

#foo just return the length of list args
def foo(a, b, c, *args):
    return len(list(args))
    
    
#bar returns a boolean value if magicnumber from kwargs meets possible value
def bar(a, b, c, **kwargs):
    if(kwargs.get("magicnumber")) == 6:
        return False
    elif(kwargs.get("magicnumber")) == 7:
        return True
    

# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")

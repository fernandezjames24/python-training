
#decorator that check argument if valid type
def type_check(correct_type):
    def funccaller(funchere):
        def newfunc(args):
            #condition that checks if args is a valid type. If the condition is true it will print "Bad Type" otherwise return and run the function
            if type(args) != correct_type:
                print("Bad Type")
            else:
                return funchere(args)
        return newfunc
    return funccaller
            
    
@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])









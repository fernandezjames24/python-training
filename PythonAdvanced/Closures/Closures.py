
#enclosing func that accept first number
def multiplier_of(number1):
  #nested function that accept second number (to be multiplied by number1)
    def multiplywith(number2):
        print(number1 * number2)
    return multiplywith


multiplywith5 = multiplier_of(5)
multiplywith5(9)


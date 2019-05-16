
# function list_benefits() returns a list of strings
def list_benefits():
    return ["More organized code","More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# function that returns a string that starts with its argument and will end
# with literal "is a benefit of functions!"
def build_sentence(info):
    return info + " is a benefit of functions!"

# main function to run
def name_the_benefits_of_functions():

    # assigning list_benefits() func to a variable (since list_benefits() returns
    # a list, list_of_benefits variable will become a list)
    list_of_benefits = list_benefits()

    # iterate through list_of_benefits elements
    for benefit in list_of_benefits:
        # prints build_sentence(benefit) function, which returns a string.
        # benefit value is an element of list_of_benefits list per successive
        # iteration
        print(build_sentence(benefit))


# call function
name_the_benefits_of_functions()


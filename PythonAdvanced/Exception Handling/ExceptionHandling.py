actor = {"name": "John Cleese", "rank": "awesome"}


def get_last_name():

    #handling exception
    try:
        return actor["last_name"]
    except:
    #if unhandled, get actor name on actor dictionary and split then return the lastname (located at index 1 of lastname variable)   
        lastname = actor["name"].split()
        return lastname[1]
        
        
    
    

#Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}





#add Jake to phonebook dictionary
phonebook["Jake"] = 938273443

#delete Jill to phonebook dictionary
phonebook.pop("Jill")



# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

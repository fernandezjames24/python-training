
#change string variable s to a string appropriate on criteria below
#the string would be "string data welcome!"

s = "String data welcome!"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Based on variable s, it has 2 a's on word "data"
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# to uppercase
print("String in uppercase: %s" % s.upper())

#to lower case
print("String in lowercase: %s" % s.lower())

# s variable starts with a string "Str" from word "String"
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# s variable ends with a string "ome!" from word "welcome!"
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# when s splitted, it contains exactly 3 words
print("Split the words of the string: %s" % s.split(" "))

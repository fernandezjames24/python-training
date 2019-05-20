#import urlopen from urllib.request to open and read from URLs
from urllib.request import urlopen
import sys

#checkvalidwords is a generator function that opens a URL text file and returns as an iterable
#I picked generator because it is lazy initialized (call in need), so it has lower memory consumption and best for big data processing
#I created two variants checkvalidwords and checkvalidwordsshort


#URL of a text file
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

#checkvalidwords simple and more friendly version
def checkvalidwords(word):
    
    for someword in urlopen(url):
        if word in someword.decode('utf-8'):
            yield someword.decode('utf-8').strip()


#shortend version of checkvalidwords using generator expression 
def checkvalidwordsshort(word):
    return(someword.decode('utf-8').strip() for someword in urlopen(url) if word in someword.decode('utf-8'))



#input word to compare with a dictionary file
a = input("Enter a word: ")
print("Output:")

#iterate through generator
for words in checkvalidwords(a):
    print(words)





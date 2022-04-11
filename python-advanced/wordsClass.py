#!/usr/bin/python3
class analysedText(object):
    
    def __init__ (self, text):

        # TODO: Remove the punctuation from <text> and make it lower case.
        self.text = text
        self.text = self.text.replace('.',' ')
        self.text = self.text.replace('!',' ')
        self.text = self.text.replace(',',' ')
        self.text = self.text.replace( '?', ' ')
        
        
    

        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = self.text.lower()
        pass 
    
    def freqAll(self,uniqueWords):    

        # TODO: Split the text into a list of words  
        wordsList = self.fmtText.split() #the result will be a list

        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        dic = {}
        for word in uniqueWords:
            countNum = wordsList.count(word)
            dic[word] = countNum
        
        return dic
        pass # return the created dictionary
    
    
    
    def freqOf(self, word):

        # TODO: return the number of occurrences of <word> in <fmtText>
        wordsList = self.fmtText.split()
        countNum = wordsList.count(word)
        return countNum

        pass

str1 = """You must? have come across! many situations when you need to pass some information 
from your browser to web server and ultimately to your CGI Program. Most frequently, browser 
uses two methods two 
pass this information to web server. These methods are GET Method and POST Method."""
s1 = analysedText(str1)
print(s1.fmtText)
list = ['you','when','and']
print(s1.freqAll(list))

print(s1.freqOf('you'))
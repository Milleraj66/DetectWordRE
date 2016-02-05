'''
    FileName:       DetectWordRE.py
    Author:         Arthur J. Miller
    Date:           02-01-2016, AJM: 02-04-2016
    Purpose:        ECE480 HW 1
                    - Develope a function that takes a string as its input and computes the frequency of every word
                    in the string and returns a dictionary that maps words in the string to their frequency
                    - Use "regular expression" in order to accomplish this task
                    - Example input: "The pure and simple truth is rarely pure and never simple"
    Inputs: String = "The pure and simple truth is rarely pure and never simple"
    Output: Dictionary = {
                            The :   1
                            pure:   2
                            and:    2
                            simple: 2
                            truth:  1
                            is:     1
                            rarely: 1
'''

#import modules
import re

def main(InputString):
    pattern = re.compile(r'\b([a-zA-Z]+)\b')
    Output = dict()
    # Scan input string for all words and store in list
    for word in re.findall(pattern, InputString):
        # If word is alread a key, increment value by one
        if(Output.has_key(word)):
            Output[word] = Output[word] + 1
        # Base Case: add key = current word, and set value to one
        else:
            Output[word] = 1
    print(Output)



# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  In = "The pure and simple truth is rarely pure and never simple"
  main(In)

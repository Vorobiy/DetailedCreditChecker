"""
PROBLEM: write a program using functions that calculates a persons credit score using the following variables: 
age(int), location(dict), citizenship(dict), previous credit score(int), average monthly spending(float), late payments(int), accounts closed(int)
the program should be able to take in input from a text file and print out a credit score as well as ways to improve the credit score.
"""

file = open("personal_info_15_people.txt")
def readInfo(): #reads the information of all people from the text file, which is seperated by an empty line.
    for line in file:
        print(line, end='')
    

def grabInfo(person): #grabs the data of the person you want to view the credit score of, and inserts it in the array "info". 
#Note: the index of a name is guaranteed to be increasing by a constant of 9, starting at 0.
    info = []
    start = person * 9 
    ending = start + 8
    text = list(file)
    text = text[start : ending]

    for i in range(len(text)): # for loop to replace the '\n' with just values.
        if '\n' in text[i]:
            text[i] = text[i].replace('\n', ' ')

    return text
        

def previousCreditScore(text): 
    initialScore = int(text[4]) #Compares the integer value of the array value at the index, beacuse the value is initially a string.

    if initialScore == 0: #Assumes if a person has a credit score of 0 that means they've never had any credit score, which sets it to 600 automatically. (use grabInfo(1) to see its effect.)
        initialScore = 600
        return initialScore
    else:
        return initialScore
    


text = grabInfo(1)
print(previousCreditScore(text))
        









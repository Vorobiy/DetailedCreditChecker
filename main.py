"""
PROBLEM:
You're a Canadian bank company looking to create a new, very biased credit score algorithm, in order to experiment
with peoples finances before the government shuts you down.

write a program using functions that calculates a persons credit score using the following variables: 
age(int), location(dict), previous credit score(int), average monthly spending(float), late payments(int), accounts closed(int)
the program should be able to take in input from a text file of peoples data and print out a credit score as well as ways to improve the credit score.
"""

file = open("personal_info_15_people.txt")
def readInfo(): # Reads the information of all people from the text file, which is seperated by an empty line.
    for line in file:
        print(line, end='')
    

def grabInfo(person): # Grabs the data of the person you want to view the credit score of, and inserts it in the array "info". 
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
    score = int(text[4]) # Compares the integer value of the array value at the index, beacuse the value is initially a string.

    if score == 0: # Assumes if a person has a credit score of 0 that means they've never had any credit score, which sets it to 600 automatically. (use grabInfo(1) to see its effect.)
        score = 600
        return score
    else:
        return score
    
def ageFactor(text, score): # the older you are, the more credit score you have, hence an age factor is implmented.
    age = int(text[1])
    i = 0
    if score == 600: # starts by giving you a credit boost if you have a new account set up, could be faulty and in need of a fix because what if a person has an account that just happens to be 600?
        while i < age: #while loop to add the score up until it creates a new score based on age. (1 year = 1 point)
            score += 1
            i += 1
        return score
    else:
        return score # if the person has had a previous account, theres no need to modify it based on age, as its been adjusted to that already.

def cityFactor(text, score): # Function that uses a dictionary to use preset points given to a city. Biased on the distance away from Toronto. (And how much I want to visit each city)
    cityValues= {"New York": 50, "Toronto": 100, "London": -10, "Sydney":20, "San Francisco":75, "Madrid":10, "Seoul":15, "Mumbai":-20,   
                  "Hanoi":20, "Melbourne": 18, "Dublin": 20, "Beijing": 35, "Stockholm": 20, "Rio de Janeiro": 10, "Rome": 25}
    city = text[2].strip() #strips the empty line in the text, need to figure out how to optimize
    if city in cityValues:
        score += cityValues[city]
    
    return score

def countryFactor(text, score): # Function that uses a dictionary to use preset points given to a country. Biased on the distance away from Toronto.
    countryValues =  {"Canada": 0, "USA": 10, "UK": 30, "Australia": 50, "Spain": 35, "South Korea": 45, 
                      "India": 40, "Vietnam": 45, "Ireland": 30, "China": 45, "Sweden": 35, "Brazil": 35, "Italy": 30}
    country = text[3].strip()
    if country in countryValues:
        score += countryValues[country]

    return score

def monthlySpendingFactor(text, score):
    initialCredit = 5000 # In this very biased world, everyone gets the same starting credit of 5000 dollars.
    spending =  float(text[5])
    if spending == 0.0: #checks to see if person spent anything at all, if not it keeps their score the same.
        return score
    elif spending <= 5000*0.3: # Did you know? Canadian banks reduce your credit score if you spend more than 30% of your monthly credit on your credit card? (Source: DMZ Startups Masterclass) and this is what this code is trying to simulate.
        score += 10 #score increases this much based on a yearly average of monthly spending, hence why the score goes up so high.
    else:
        score += -10
    return score

def latePaymentsFactor(text, score): # Function that exponentially lowers their credit score based on their amount of late payments.
    latePayments = int(text[6])

    if latePayments == 0: #If theres no late payments, why bother with a loop? returns score from previous factors.
        return score
    else:
        for i in range(1, latePayments+1): # With every missed payment, your credit score goes down by 20 * number of latepayments
            score = score - 20 * i

    return score

def accountsClosedFactor(text, score): # A Function that decreases the score by 20 with every account closed
    closed = int(text[8])
    i = 0
    if closed == 0:
        return score
    else:
        while i <= closed:
            score += -20 
    return score

def limiter(score): #Puts a limit on how much credit score a person can have, between 300 and 900. (Reinforces the idea of score = 0 in the beginning being a new account.)
    if score > 900:
        score = 900
    if score < 300:
        score = 300
    else:
        return score
    return score

text = grabInfo(14) #modify the value inside from 0-14 to index into different people
print(text)
score = previousCreditScore(text)
score = ageFactor(text, score)
score = cityFactor(text, score)
score = countryFactor(text,score)
score = monthlySpendingFactor(text,score)
score = latePaymentsFactor(text,score)
score = limiter(score)
print("Final Credit Score:", score)
        









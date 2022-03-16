#============================================================================================#

# Descrition: Utilizes REST Countries API to randomly get city data for quiz question and answer.
# Author: James Garrick

#============================================================================================#

import requests as r
import random
import json

#============================================================================================#

questionsAnswered = 0
triesAllowed = 2
cheatMode = False

#============================================================================================#

countryList = r.get("https://restcountries.com/v3.1/all?fields=name,capital,continents")
country = random.choice(json.loads(countryList.content))
cName = country['name']['common']
cCapital = country['capital']
cContinent = country['continents']

#============================================================================================#

def question(question, answer):
    global questionsAnswered
    global triesAllowed
    
    print('\n' + str(question))
    
    if cheatMode == True:
        print('(The answer is ' + str(answer) + '.)')
    
    ans = input('\n   > ').lower()
    if ans.lower() == answer.lower():
        print('\n Correct!')
        questionsAnswered += 1
    else: 
        print('\n Incorrect, the answer is ' + str(answer) + '.')
        #question(question, answer)
    
#============================================================================================#

# Defines all questions.

question('What is the capital of ' + str(cName) + '?', cCapital[0])
question('What continent is ' + str(cName) + ' located in?', cContinent[0])

#============================================================================================#
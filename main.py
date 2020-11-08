# Where to run the program from

import random
import UI
import logic

# number of questions per category
numQs = 5

# number of categories
numCats = 5

# total number of questions (currently 25)
totalQs = numQs * numCats

# list of categories
categories = ["bill", "budget", "credit", "invest", "loans"]

# categories (keys) and number of questions remaining  (values) in each
remaining = {}
# initializes it
for i in range(numCats):
    remaining[categories[i]] = numQs

UI.displayInstruction()
UI.play()

asked = 0

while asked < totalQs:
    # picks a random category
    randCat = categories[random.randint(0,numCats-1)]
    qRemaining = remaining[randCat]

    # checks if there are questions left in this category
    # if there aren't, start over
    if qRemaining <= 0:
        continue

    # updates values so this upcoming question won't be asked again
    remaining[randCat] = qRemaining - 1
    #asked += 1

    # asks question, takes in answer, and displays correction
    questionsNode = UI.displayQuestion(randCat)
    if logic.validQuestionsNode(questionsNode) == True:
        userAnswer = UI.displayInput()
        UI.displayCorrection(questionsNode, userAnswer)
        asked += 1
    print()

    # checks if there are questions left in this category
    #if qRemaining > 0:
        #remaining[randCat] = qRemaining - 1
        #asked += 1

UI.displayResult()
import logic

def displayInstruction():
    print("""Welcome to the Financial Literacy Contest!  You have been given $100 to start.  
            The goal is to keep as much money as possible by the end of the upcoming examination.

            There are five categories: budgeting and setting financial goals; paying bills, taxes,
            and saving money; loans; credit; and investing, 401(k)s, and stocks.
            Each of these categories is worth $20.
            
            There are a total of 25 questions, 5 per category.  Each question is worth $4.
            
            Good luck!""")

def play():
    #todo 2: add code here to control how the user interacts / plays the game
    print(""" You will see multiple choice questions printed on the console.  To respond, 
            #simply type in the letter of the correct answer (A, B, C, or D).""")

    # questionInfo = {}
    # #an example of credit questions
    # while True:
    #     questionInfo = logic.getQuestionInfo("credit")
    #     if questionInfo == {}:
    #         break
    #     else:
    #         #display question
    #         print("\n", questionInfo["question"])

    #         #display all answer choice
    #         for choice in questionInfo["choices"]:
    #             print("\n", choice)

# Displays the final game result
def displayResult():
    #todo 3: display the final game result"
    print("Congratulations, you have completed the exam!  You have $") # + sum "remaining"
    # or instead say how much money you lost (or both?)?
    print("Here is your breakdown by category: ")
    print("    Budgeting and setting financial goals: ") # + this sum
    print("    Paying bills, taxes, and saving money: ") # + this sum
    print("    Credit...............................: ") # + this sum
    print("    Investing, 401(k)s, and stocks.......: ") # + this sum

# displays if the user was correct or incorrect and how much money they have
# inputs the question node and user's inputted answer it is correcting for
def displayCorrection(questionsNode, answer):
    # Check if answer is correct:
    category = logic.getCategory(questionsNode)
    question = logic.getQuestion(questionsNode)

    if logic.checkAnswer(category, question, answer) == True:
        print("Correct!")
    # Makes correction if incorrect
    else:
        correctAnswer = logic.getCorrectAnswer(questionsNode)
        reference = logic.getReference(questionsNode)
        print("Incorrect (-$4).  The correct answer was " + correctAnswer) # + answer from json
        print("You can learn about this topic here: " + reference)

    print("Your total sum is now $") 
    # + new sum

# displays a question and the answers from a specific category and 
# returns the question node these came from
def displayQuestion(category):
    questionInfo = logic.getQuestionInfo(category)
    if logic.validQuestionsNode(questionInfo):
        question = logic.getQuestion(questionInfo)
        print(question)
        answers = logic.getAnswers(questionInfo)
        for answer in answers:
                for key, value in answer.items():
                    print("{}: {}".format(key, value))
    return questionInfo

# prompts the user to input their answer and returns this
def displayInput():
    while (True):
        answer = input("Enter your answer here: ")
        if answer.lower() in ["a", "b", "c", "d"]:
            return answer
        else:
            print("Answer not valid.  Must be A, B, C, or D and only one letter.")

# Testing:
testing = True
if (testing):
    questionsNode = displayQuestion("credit")
    answer = displayInput()
    displayCorrection(questionsNode, answer)

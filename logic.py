import random
import copy
import data
from data import data_bill, data_budget, data_credit, data_invest, data_loans


# data backup due to deletiion during the getQuestionInf()
data_budget_copy = copy.deepcopy(data_budget.data)
data_bill_copy = copy.deepcopy(data_bill.data)
data_loans_copy = copy.deepcopy(data_loans.data)
data_credit_copy = copy.deepcopy(data_credit.data)
data_invest_copy = copy.deepcopy(data_invest.data)

# inputs a category and makes a dict from the corresponding json object
# chooses a random question node, returns it, and removes it from the dict
def getQuestionInfo(category):
    # makes dictionary from corresponding category JSON file
    data = data_budget.data
    if category == "budget":
        data = data_budget.data
    elif category == "bill":
        data = data_bill.data
    elif category == "loan": 
        data = data_loans.data
    elif category == "credit":
        data = data_credit.data
    elif category == "invest":
        data = data_invest.data

    # chooses random question node to return and remove from dict
    random_question = {}
    length = len(data['questions'])
    if length != 0:
        index = random.randint(0,length-1) 
        random_question = data["questions"][index]
        data["questions"].pop(index)

    return random_question

# 
def checkAnswer(category, question, answer):
    accuracy = False

    data = data_budget.data
    if category == "budget":
        data = data_budget_copy
    elif category == "bill":
        data = data_bill_copy
    elif category == "loan": 
        data = data_loans_copy
    elif category == "credit":
        data = data_credit_copy
    elif category == "invest":
        data = data_invest_copy

    for questionInfo in data["questions"]:
        if questionInfo["question"] == question:
            if questionInfo["answer"] == answer:
                accuracy = True
            
            break

    return accuracy

def getScore():
    #todo: get the score 
    print("todo")
    return

# checks if a questions node is empty, true if isn't, false if is
def validQuestionsNode(node):
    if node == {}:
        return False
    else:
        return True

# extracts the question as a string from a questions node
def getQuestion(questionsNode):
    question = questionsNode["question"]
    return question

# extracts the answer choices as a list from a questions node
def getAnswers(questionsNode):
    answers = []
    for answer in questionsNode["choices"]:
        answers.append(answer)
    return answers

# extracts the reference as a string from a questions node
def getReference(questionsNode):
    reference = questionsNode["reference"]
    return reference

# extracts the category as a string from a questions node
def getCategory(questionsNode):
    category = questionsNode["category"]
    return category

def getCorrectAnswer(questionsNode):
    correctAnswer = questionsNode["answer"]
    return correctAnswer

# Tests:
testing = False
#accuracy = checkAnswer("credit", "The best way to pay off credit card debt is: ", "C")
#print (accuracy)
if (testing):
    for i in range(10):
        node = getQuestionInfo("credit")
        if validQuestionsNode(node):
            #print(node)
            print(getQuestion(node))
            answers = getAnswers(node)
            #for answer in answers:
                #print(answer)
            #for key, value in answers.items():
                #print("{}: {}".format(key, value))
            # print answers in formatted fashion
            for answer in answers:
                for key, value in answer.items():
                    print("{}: {}".format(key, value))
            #print(getReference(node))
            # add new line before next question
            print()
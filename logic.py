import random
import copy
#import data_bill
#import data_budget
#import data_credit
#import data_invest
#import data_loans

import data
from data import data_bill, data_budget, data_credit, data_invest, data_loans


# data backup due to deletiion during the getQuestionInf()
data_budget_copy = copy.deepcopy(data_budget.data)
data_bill_copy = copy.deepcopy(data_bill.data)
data_loans_copy = copy.deepcopy(data_loans.data)
data_credit_copy = copy.deepcopy(data_credit.data)
data_invest_copy = copy.deepcopy(data_invest.data)


def getQuestionInfo(category):
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
        
    random_question = {}
    length = len(data['questions'])
    if length != 0:
        index = random.randint(0,length-1) 
        random_question = data["questions"][index]
        data["questions"].pop(index)

    return random_question

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


#accuracy = checkAnswer("credit", "The best way to pay off credit card debt is: ", "C")
#print (accuracy)


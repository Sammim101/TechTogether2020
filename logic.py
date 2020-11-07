import data_bill
import data_budget
import data_credit
import data_invest
import data_loans
import random
import copy

# data backup due to deletiion during the getQuestionInf()
data_budget_copy = copy.deepcopy(data_budget.data)
data_bill_copy = copy.deepcopy(data_bill.data)
data_loan_copy = copy.deepcopy(data_loan.data)
data_credit_copy = copy.deepcopy(data_credit.data)
data_invest_copy = copy.deepcopy(data_invest.data)

def getQuestionInfo(category):
    data = data_budget.data
    if category == "budget":
        data = data_budget.data
    elif category == "bill":
        data = data_bill.data
    elif category == "loan": 
        data = data_loan.data
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
    accuracy = false





    return

def getScore():
    #todo: get the score 
    print("todo")
    return

def determineData(category):
        data = data_budget.data
    if category == "budget":
        data = data_budget.data
    elif category == "bill":
        data = data_bill.data
    elif category == "loan": 
        data = data_loan.data
    elif category == "credit":
        data = data_credit.data
    elif category == "invest":
        data = data_invest.data





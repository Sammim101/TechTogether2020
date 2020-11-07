import logic

def displayInstruction():
    print("todo 1: display game instruction")

def play():
    questionInfo = {}
    #an example of credit questions
    while True:
        questionInfo = logic.getQuestionInfo("credit")
        if questionInfo == {}:
            break
        else:
            #display question
            print("\n", questionInfo["question"])

            #display all answer choice
            for choice in questionInfo["choices"]:
                print("\n", choice)


def displayResult():
    print ("todo 3: display the final game result")

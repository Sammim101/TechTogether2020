import json

data = {
    "questions":[
        {
            "question" : "Should you automate finances and why?", 
            "category" : "bill", 
            "choices":[
                {"A" : "Yes. It keeps your financial accounts organized and saves time on accounting."},
                {"B" : "Yes.  It protects credit by ensuring bills are paid on time and allows you to maximize interest."},
                {"C" : "No.  It is too easy to fall into debt without managing your finances yourself."},
                {"D" : "A and B."}
            ],
            "answer" : "D",
            "reference" : "https://www.financialeducatorscouncil.org/national-financial-capability-test/ "
        },        
        {
            "question" : "How do you automate your finances?", 
            "category" : "bill", 
            "choices":[
                {"A" : "Just open up a checking and savings account.  The rest will be taken care of for you."},
                {"B" : "First open a checking account with a cash cushion,then set up direct deposit from your employer, then “pay yourself first,” set bills on autopay, then set up automatic investing, and finally set up automatic escalation."},
                {"C" : "Do everything in B except for setting up automatic escalation."},
                {"D" : "You should not automate your finances."},
            ],
            "answer" : "B",
            "reference" : "https://www.forbes.com/sites/peterlazaroff/2018/01/17/how-to-automate-your-finances-in-5-easy-steps/?sh=31e5dca0329a"
        },
        {
            "question" : "What does it mean to “pay yourself first” and why should you do it?", 
            "category" : "bill", 
            "choices":[
                {"A" : "When your paycheck is deposited to your checking account, it should be directed to your emergency funds, retirement savings, and other savings accounts.  This will keep you financially stable by increasing your savings."},
                {"B" : "You should not “pay yourself first”."},
                {"C" : "When your paycheck is deposited to your checking account, you should spend money on consumer items you enjoy.  This will keep you happier and more productive."},
                {"D" : "When your paycheck is deposited to your checking account, you should remove it from the bank.  This is because keeping money in the bank is not safe."},
            ],
            "answer" : "A",
            "reference" : "https://www.doughroller.net/personal-finance/the-complete-guide-to-automating-your-finances/ and https://www.forbes.com/sites/peterlazaroff/2018/01/17/how-to-automate-your-finances-in-5-easy-steps/?sh=31e5dca0329a "
        },
        {
            "question" : "What is automatic escalation and why should you do it?", 
            "category" : "bill", 
            "choices":[
                {"A" : "Increases the amount of money you contribute to your 401(k) over time, resulting in less savings."},
                {"B" : "Decreases the amount of money you contribute to your 401(k) over time, resulting in less savings."},
                {"C" : "Decreases the amount of money you contribute to your 401(k) over time, resulting in more savings."},
                {"D" : "Increases the amount of money you contribute to your 401(k) over time, resulting in more savings"},
            ],
            "answer" : "D",
            "reference" : "https://money.usnews.com/investing/articles/2017-06-23/build-a-better-401k-balance-with-auto-escalation"
        },
        {
            "question" : "What organization is in charge of tax collection and does it provide resources to help you?", 
            "category" : "bill", 
            "choices":[
                {"A" : "The International Receipt Service (IRS), it has just a few resources."},
                {"B" : "The Tax Collection Committee (TCC), it provides a lot of resources."},
                {"C" : "The Internal Revenue Service (IRS), it provides a lot of resources."},
                {"D" : "The Tax Collection Committee (TCC), it does not provide resources."},
            ],
            "answer" : "C",
            "reference" : "https://www.irs.gov/"
        }
    ] 
}
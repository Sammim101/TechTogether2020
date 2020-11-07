import json

data = {
    "questions":[
        {
            "question" : "What is a 401(k) plan?", 
            "category" : "invest", 
            "choices":[
                {"A" : "A government-qualified, employer-sponsored retirement savings plan in which employees receive a retirement savings package from employers."},
                {"B" : "A government-qualified, employer-sponsored spending plan that guides employees in making major spending decisions."},
                {"C" : "A government-qualified employer-sponsored retirement savings plan in which employees choose to invest money in mutual funds."},
                {"D" : "A non-government qualified employee-sponsored financial plan to help fellow employees."}
            ],
            "answer" : "C",
            "reference" : "https://www.investopedia.com/articles/retirement/08/401k-info.asp and https://guides.wsj.com/personal-finance/retirement/what-is-a-401k/ "
        },        
        {
            "question" : "What is a Roth versus Traditional 401(k) plan?", 
            "category" : "invest", 
            "choices":[
                {"A" : "Roth: suggested for younger investors who will be earning a bigger salary in the future, contributions made after tax, withdrawals are tax-free.  Traditional: contributions made pre-tax (there’s an upfront tax reduction), but you are taxed on withdrawal. Choosing: It is possible to pick either one or both."},
                {"B" : "Roth: contributions made after tax, withdrawals are tax-free.  Traditional: suggested for younger investors who will be earning a bigger salary in the future, contributions made pre-tax (there’s an upfront tax reduction), but you are taxed on withdrawal.  Choosing: It is possible to pick either one or both."},
                {"C" : "Roth: suggested for younger investors who will be earning a bigger salary in the future, contributions made after tax, withdrawals are tax-free.  Traditional: contributions made pre-tax (there’s an upfront tax reduction), but you are taxed on withdrawal. Choosing: you have to pick one or the other."},
                {"D" : "Roth: suggested for younger investors who will be earning a bigger salary in the future, contributions made pre-tax (there’s an upfront tax reduction), but you are taxed on withdrawal.  Traditional: contributions made after tax, withdrawals are tax-free.  Choosing: you have to pick one or the other."},
            ],
            "answer" : "A",
            "reference" : "https://www.schwab.com/resource-center/insights/content/roth-vs-traditional-401-k-which-is-better "
        },
        {
            "question" : "Suppose you invest $2,500 and earn 7% per year on this investment.  How many years will it take for your total investment to be worth $5,000?", 
            "category" : "invest", 
            "choices":[
                {"A" : "Between 0 and 5 years."},
                {"B" : "Between 5 and 15 years."},
                {"C" : "15+ years."},
                {"D" : "Indeterminable fro.m information provided"},
            ],
            "answer" : "B",
            "reference" : "http://online.wsj.com/public/resources/documents/FinLitQuizAnswsersv4.pdf "
        },
        {
            "question" : "Suppose you and your employer contribute every year to your employer-sponsored 401(k). You have worked at the company for twenty years and are fully vested in your plan. Which of the following are true?", 
            "category" : "invest", 
            "choices":[
                {"A" : "If you no longer work for the company, the whole plan balance is forfeited because your benefits are tied to the job."},
                {"B" : "If you get fired, the company has the right to decide how much of your total plan balance you will get."},
                {"C" : "If you voluntarily leave your job, you forfeit all of your employer’s contributions."},
                {"D" : "Even if you leave your job or get fired, you are still entitled to the entire plan balance."},
            ],
            "answer" : "D",
            "reference" : "http://online.wsj.com/public/resources/documents/FinLitQuizAnswsersv4.pdf"
        },
        {
            "question" : "What is the difference between stock mutual funds/ETFs and individual stocks as well as some of their advantages and disadvantages?", 
            "category" : "invest", 
            "choices":[
                {"A" : "Mutual fund/ETF: shares from a specific company.  Advantages: chance to make major profit off wise picks.  Disadvantages: much riskier, time-intensive. Individual stocks: a collection of small pieces of many different stocks.  Better for the majority of investors. Advantages: diversified and therefore safer, less time-intensive.  Disadvantages: less potential for major gains."},
                {"B" : "Mutual fund/ETF: a collection of small pieces of many different stocks. Advantages: chance to make major profit off wise picks.  Disadvantages: much riskier, time-intensive. Individual stocks: shares from a specific company. Better for the majority of investors. Advantages: diversified and therefore safer, less time-intensive.  Disadvantages: less potential for major gains."},
                {"C" : "Mutual fund/ETF: a collection of small pieces of many different stocks.  Better for the majority of investors. Advantages: diversified and therefore safer, less time-intensive.  Disadvantages: less potential for major gains. Individual stocks: shares from a specific company.  Advantages: chance to make major profit off wise picks.  Disadvantages: much riskier, time-intensive."},
                {"D" : "None of the above."},
            ],
            "answer" : "C",
            "reference" : "https://www.nerdwallet.com/article/investing/how-to-invest-in-stocks, https://www.moneycrashers.com/mutual-fund-types-pros-cons/, and https://www.investopedia.com/articles/investing/072915/single-stocks-your-portfolio-pros-and-cons.asp."
        }
    ] 
}
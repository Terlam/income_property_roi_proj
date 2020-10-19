class IncomeProperty:
    def __init__(self,monthlyIncome,monthlyExpenses,cashInvestment):
        self.monthlyIncome = monthlyIncome
        self.monthlyExpenses = monthlyExpenses
        self.cashInvestment = cashInvestment


    def cashCalc(self):
        self.monthlyIncome =int(input("Give the total monthly income: "))
        self.monthlyExpenses = int(input("Give the total monthly expenses: "))
        self.cashInvestment = int(input("How much cash did you initially invest in the property?: "))
        self.cashFlow = self.monthlyIncome - self.monthlyExpenses
        self.roi = float((self.cashFlow * 12)/self.cashInvestment)
        self.viewRoi= "{:.2%}".format(self.roi)
        print(f'your monthly cash flow is {self.cashFlow}')
        print(f'your annual return on investment is {self.viewRoi}')
     
house = IncomeProperty("","","")

def run():
    while True:
        response = input('Lets find out the ROI on a property. \nTo start type "start": ')
        if response.lower() == "start":
            house.cashCalc()
       
run()
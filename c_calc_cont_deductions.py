from b_main_deductions_corporate import corp_deductions as cdc
from b_main_deductions_income import salary_deductions as sdc
from b_main_deductions_dividends import div_deductions as ddc

class calc_deductions:
    
    def __init__(self,turnover,salary,expenses):
        
        self.turnover = turnover
        self.salary = salary
        self.expenses = expenses
        
    def expenses(self):
        
        return(cdc(self.turnover,self.salary,self.expenses).total_exp())
        
    def corp_tax(self):
        
        return(cdc(self.turnover,self.salary,self.expenses).corp_tax())
    
    def corp_ni(self):
        
        return(cdc(self.turnover,self.salary,self.expenses).corp_ni())
    
    def dividend(self):
        
        if cdc(self.turnover,self.salary,self.expenses).net_profit() < 0:
            return(0)
        else:
            return(cdc(self.turnover,self.salary,self.expenses).net_profit())
    
    def dividend_tax(self):
        
        return(ddc(self.dividend()).div_tax())
        
    def income_tax(self):
        
        return(sdc(self.salary,0,0).salary_tax())
        
    def income_ni(self):
        
        return(sdc(self.salary,0,0).salary_ni())
    
    def total_deductions(self):
        
        return(self.income_tax() + self.income_ni() + self.dividend_tax() + self.corp_ni() + self.corp_tax())
    
    def gross_takehome(self):
        
        return(self.salary + self.dividend())
    
    def total_takehome(self):
                
        return(ddc(self.dividend()).div_th() + sdc(self.salary,0,0).sal_th())

# t = 55000
# s = 60000
# e = 3000

# print("income tax............",calc_deductions(t,s,e).income_tax())

# print("income ni.............",calc_deductions(t,s,e).income_ni())

# print("dividend tax..........",calc_deductions(t,s,e).dividend_tax())

# print("corp ni...............",calc_deductions(t,s,e).corp_ni())

# print("corp_tax..............",calc_deductions(t,s,e).corp_tax())

# print("dividend..............",calc_deductions(t,s,e).dividend())

# d = calc_deductions(t,s,e).dividend()

# print("total_deduction.......",calc_deductions(t,s,e).total_deductions())

# print("st_loan...............",sdc((d+s),0,1).st_loan())

# print("gross takehome........",calc_deductions(t,s,e).gross_takehome())

# print("total_takehome........",calc_deductions(t,s,e).total_takehome())
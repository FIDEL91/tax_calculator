#all calculations for corporate tax calculations

from calc_marginals import marginal_calc as mc

class corp_deductions:
    
    def __init__(self,turnover,salary,expenses):
        
        self.turnover = turnover
        self.salary = salary
        self.expenses = expenses
        
    def total_exp(self):
        
        exp_tot = self.salary + self.expenses
        
        return(exp_tot)
    
    def gross_profit(self):
        
        self.gross_p = self.turnover - self.total_exp()
        
        return(self.gross_p)
    
    def corp_tax(self):
        
        self.corp_tax = mc(self.gross_profit(),10).calculate()
        
        return(self.corp_tax)
    
    def corp_ni(self):
        
        self.corp_ni = mc(self.gross_profit(),8).calculate()
        
        return(self.corp_ni)
    
    def tot_ded(self):
        
        self.total_deductions = self.corp_ni() + self.corp_tax()

        return(self.total_deductions)
    
    def net_profit(self):
        
        self.net_prof = self.gross_profit() - self.tot_ded()
        
        return(self.net_prof)
    
    def takings(self):
        
        self.take = self.turnover - self.net_profit()
        
        return(self.take)

from a_calc_marginals import marginal_calc as mc

class corp_deductions:
    
    def __init__(self,turnover,salary,expenses):
        
        self.turnover = turnover
        self.salary = salary
        self.expenses = expenses
        
    def total_exp(self):
        
        return(self.salary + self.expenses)
        
    def gross_profit(self):
        
        return(self.turnover - self.total_exp())
    
    def corp_tax(self):
        
        return(mc(self.gross_profit(),10).calculate())
    
    def corp_ni(self):
        
        return(mc(self.salary,8).calculate())
    
    def tot_ded(self):
        
        return(self.corp_ni() + self.corp_tax())

    def net_profit(self):
        
        return(self.gross_profit() - self.tot_ded())

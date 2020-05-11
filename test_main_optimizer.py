
from tax_law_uk_2019_2020 import uk_law as law
import calc_marginals as cm
from main_deductions_corporate import corp_deductions as mdc
from main_deductions_income import salary_deductions as sdc
from main_deductions_dividends import div_deductions as ddc

class calc_deductions:
    
    def __init__(self,turnover,salary,expenses):
        
        self.turnover = turnover
        self.salary = salary
        self.expenses = expenses
        
    def tot_deds(self):
        
        self.a = mdc(self.turnover,self.salary,self.expenses).net_profit()
        
        b = ddc(self.a).div_tax()
        
        c = sdc(self.salary,0,0).salary_tax()
        
        d = sdc(self.salary,0,0).salary_ni()
        
        self.tot_ded = c
        
        return(self.tot_ded)
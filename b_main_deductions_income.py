from a_calc_marginals import marginal_calc as mc
from a_calc_percentage import percentage as pct
from a_calc_changed_allowance import new_allowance as na

class salary_deductions:
    
    def __init__(self,salary,pension,student_loan):
        
        self.salary = salary
        self.pension = pension
        self.student_loan = student_loan
        
    def pension_cont(self):
        
        return(pct(self.salary,self.pension).calculate())


    def p_pen_gross(self):
        
        return(self.salary - self.pension_cont())
    
    
    def st_loan(self):
        
        if self.student_loan == 0:
            self.sl_bill = 0
            
        if self.student_loan == 1:
            self.sl_bill = mc(self.salary,4).calculate()
            
        elif self.student_loan == 2:
            self.sl_bill = mc(self.salary,6).calculate()
        
        return(self.sl_bill)
    
    
    def salary_ni(self):
        
        return(mc(self.salary,2).calculate())


    def salary_tax(self):
        
        return(mc(self.p_pen_gross(),0).calculate())


    def total_deds(self):
        
        return(self.salary_ni() + self.salary_tax())


    def sal_th(self):
        
        return(self.p_pen_gross() - self.total_deds())
from tax_law_uk_2019_2020 import uk_law as law
from calc_marginals import marginal_calc as mc
from calc_percentage import percentage as pct
from calc_changed_allowance import new_allowance as na

class salary_deductions:
    
    def __init__(self,salary,pension,student_loan):
        
        self.salary = salary
        self.pension = pension
        self.student_loan = student_loan
        
    def pension_contribution(self):
        
        self.pension_cont = pct(self.salary,self.pension).calculate()
        
        return(self.pension_cont)
    
    def post_pension_gross(self):
        
        self.pp_gross = self.salary - self.pension_contribution()
        
        return(self.pp_gross)
    
    def st_loan(self):
        
        if self.student_loan == 0:
            self.sl_bill = 0
            
        if self.student_loan == 1:
            self.sl_bill = mc(self.post_pension_gross(),4).calculate()
            
        elif self.student_loan == 2:
            self.sl_bill = mc(self.post_pension_gross(),6).calculate()
        
        return(self.sl_bill)
    
    def salary_ni(self):
        
        self.ni = mc(self.salary,2).calculate()
        
        return(self.ni)
    
    def salary_tax(self):
        
        a = law.tax_b  
        tf_ch = law.acv
        ratio = law.acv_ratio
        
        if self.post_pension_gross() > tf_ch:
            if self.post_pension_gross() < (tf_ch + 2*a[1]):
                self.tf_amount = self.post_pension_gross() - tf_ch
        
                self.tf_reduction = self.tf_amount/ratio
        
                a[1] = a[1] - self.tf_reduction
                
            elif self.post_pension_gross() > (tf_ch + 2*a[1]):
                a[1] = 0

        self.tax = mc(self.post_pension_gross(),0).calculate()
        
        return(self.tax)
    
    def total_deductions(self):
        
        self.total_deds = self.salary_ni() + self.salary_tax()

        return(self.total_deds)
    
    def sal_th(self):
        
        self.sal_th = self.post_pension_gross() - self.total_deductions()
        
        return(self.sal_th)
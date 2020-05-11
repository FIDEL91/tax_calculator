#all calculations for dividend tax calculations

from calc_marginals import marginal_calc as tax

class div_deductions:
    
    def __init__(self,div):
        
        self.div = div
    
    def div_tax(self):
        
        self.dividend_tax = tax(self.div,12).calculate()
        
        return(self.dividend_tax)
    
    def div_th(self):
        
        self.div_th = self.div - self.div_tax()
        
        return(self.div_th)

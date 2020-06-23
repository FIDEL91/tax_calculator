from a_calc_marginals import marginal_calc as tax

class div_deductions:
    
    def __init__(self,div):
        
        self.div = div
    
    def div_tax(self):
        
        return(tax(self.div,12).calculate())
    
    def div_th(self):
        
        return(self.div - self.div_tax())
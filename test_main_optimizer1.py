from tax_law_uk_2019_2020 import uk_law as law
from test_main_optimizer import calc_deductions as cd

class optimize:
    
    def __init__(self,turnover,expenses):
        
        self.turnover = turnover
        self.expenses = expenses
        
    def opt(self):
        
        lst = []
        
        for i in range(0,self.turnover,10):
            x = cd(self.turnover,i,self.expenses).tot_deds()
            lst.append([i,x])
            
        return(lst)
    
t = 20000
e = 3000

a = optimize(t,e).opt()

print(a)
from c_calc_cont_deductions import calc_deductions as cont

class optimize:
    
    def __init__(self,turnover,expenses):
        
        self.turnover = turnover
        self.expenses = expenses
        
    def gross_takings(self):
        
        return(self.turnover - self.expenses)
    
    def salary(self):
        
        lst1 = []
        
        for i in range(1000,3000,1000):
            lst1.append(cont(self.turnover,i,self.expenses).total_takehome())
        
        return(lst1)
    
    def takehome(self):
        
        return(self.salary())
        
        
a = 100000
b = 5000

print(optimize(a,b).gross_takings())

print(optimize(a,b).salary())

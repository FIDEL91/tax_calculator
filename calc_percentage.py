#this calculates the percentage of a number. it is used to calculate how much of a salary is invested in pensions.

class percentage:
    
    def __init__(self,number,percentage):
        
        self.number = number
        self.percentage = percentage
        
    def calculate(self):
        
        answer = (self.number*self.percentage)/100
                
        return(answer)


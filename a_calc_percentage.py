#Salary Tax Calculator
class percentage:
    
    def __init__(self,number,percentage):
        
        self.number = number
        self.percentage = percentage
        
    def calculate(self):
        
        answer = (self.number*self.percentage)/100
                
        return(answer)


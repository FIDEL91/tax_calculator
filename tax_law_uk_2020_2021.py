#Not accurate at the point  of this version! this just contains the tax laws of th UK in list formats. It also contains values for the change in tax free allowances when you earn over a certain amount.

class uk_law:
    
    #UK Salary Tax, NI Brackets
    tax_b = [0,12500,50000,150000]
    tax_pc = [0,0.2,0.4,0.45]
    
    ni_b = [0,8632,50000]
    ni_pc = [0,0.12,0.02]
    
    
    #UK Student Loan Repayments
    sl_plan_1_b = [0,18935]
    sl_plan_1_t = [0,0.09]
    sl_plan_2 = [0,25725]
    sl_plan_2_t = [0,0.09]
    
    #UK Corporation NI
    cni_b = [0]
    cni_pc = [0.138]
    
    
    #UK Corpoarate Tax
    ctax_pc = 0.19
    
    
    #Dividend Thresholds
    div_b = [2000,50000,150000]
    div_pc = [0,0.075,0.325,0.381]

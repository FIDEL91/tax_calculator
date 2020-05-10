class uk_law:
    
    #Income Tax Brackets
    tax_b = [0,12500,50000,150000]
    tax_pc = [0,0.2,0.4,0.45]
    
    #National Insurance Brackets
    ni_b = [0,8632,50000]
    ni_pc = [0,0.12,0.02]
    
    #Allowance Change Value (Tax)
    acv = 100000
    acv_ratio = 2
    
    #UK Student Loan Repayments
    #Plan 1
    sl_plan_1_b = [0,18935]
    sl_plan_1_pc = [0,0.09]
    
    #Plan 2
    sl_plan_2_b = [0,25725]
    sl_plan_2_pc = [0,0.09]
    
    #UK Corporation National Insurance
    cni_b = [0]
    cni_pc = [0.138]

    #UK Corpoarate Tax
    ctax_b = [0]
    ctax_pc = [0.19]
    
    #Dividend Thresholds
    div_b = [0,2000,50000,150000]
    div_pc = [0,0.075,0.325,0.381]
    
    #Zero
    zero = [0]
    
    #List of Lists Above
    law_list = [tax_b,tax_pc,ni_b,ni_pc,sl_plan_1_b,sl_plan_1_pc,sl_plan_2_b,sl_plan_2_pc,cni_b,cni_pc,ctax_b,ctax_pc,div_b,div_pc]
    
    # Codes
    # Tax: 0
    # NI: 2
    # Student Loan P1: 4
    # Student Loan P2: 6
    # Corporate National Insurance: 8
    # Corporate Tax: 10
    # Dividend Tax: 12
    
print(type(uk_law.tax_b[1]))
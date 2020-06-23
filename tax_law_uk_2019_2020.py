class uk_law:
    
    #Income Tax Brackets
    
    #0
    tax_b = [0,12500,50000,150000]
    #1
    tax_pc = [0,0.2,0.4,0.45]
    
    #National Insurance Brackets
    
    #2
    ni_b = [0,8632,50000]
    #3
    ni_pc = [0,0.12,0.02]
    
    #UK Student Loan Repayments
    #Plan 1
    
    #4
    sl_plan_1_b = [0,18935]
    #5
    sl_plan_1_pc = [0,0.09]
    
    #Plan 2
    #6
    sl_plan_2_b = [0,25725]
    #7
    sl_plan_2_pc = [0,0.09]
    
    #UK Corporation National Insurance
    
    #8
    cni_b = [0]
    #9
    cni_pc = [0.138]

    #UK Corpoarate Tax
    
    #10
    ctax_b = [0]
    #11
    ctax_pc = [0.19]
    
    #Dividend Thresholds
    
    #12
    div_b = [0,2000,50000,150000]
    #13
    div_pc = [0,0.075,0.325,0.381]
    
    
    #Allowance Change Value (Tax)
    acv = 100000
    acv_ratio = 2
    
    
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

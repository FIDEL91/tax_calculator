from tax_law_uk_2019_2020 import uk_law as law
import calc_marginals as cm
from main_deductions_corporate import corp_deductions as mdc
from main_deductions_income import salary_deductions as sdc
from main_deductions_dividends import div_deductions as ddc

a = 25652.5
b = 0
c = 0

d = []

p = 0
sl = 0

for i in range(0,int(a-c),10):
    x = mdc(a,i,c).takings()
    x3 = sdc(i,p,sl).sal_th()
    x2 = ddc(mdc(a,i,c).net_profit()).div_th()
    d.append([i,x2])
        
print(d)

print(max(d))

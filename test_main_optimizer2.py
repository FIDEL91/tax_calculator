# just a test program (not required)


from tax_law_uk_2019_2020 import uk_law as law
import calc_marginals as cm
from main_deductions_corporate import corp_deductions as mdc
from main_deductions_income import salary_deductions as sdc
from main_deductions_dividends import div_deductions as ddc

salary = 50000

c = sdc(salary,0,0).salary_tax()

d = sdc(salary,0,0).salary_ni()

tot_ded = c + d

print(tot_ded)

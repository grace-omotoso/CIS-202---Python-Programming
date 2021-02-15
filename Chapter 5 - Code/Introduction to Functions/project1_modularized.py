# A program that computes the net pay of an employee
RATE1 = 0.10
RATE2 = 0.12
RATE3 = 0.22
RATE4 = 0.24
RATE5 = 0.32
RATE6 = 0.35
RATE7 = 0.37
FICA_SS = 0.062 #  6.2%
FICA_MEDICARE = 0.0145 # 1.45%

# Get input
def get_input():
    gross_pay = float(input("Enter the monthly gross pay: "))
    ins_prem =  float(input("Enter the monthly health insurance premium: "))
    other_deduc = float(input("Enter other deductions: "))

    return gross_pay, ins_prem, other_deduc

# COMPUTE THE TAX
def compute_tax(gross_pay):
    if gross_pay >= 43200:
        tax = RATE7*gross_pay
    elif gross_pay >= 17300:
        tax = RATE6*gross_pay
    elif gross_pay >= 13600:
        tax = RATE5*gross_pay
    elif gross_pay >= 7200:
        tax = RATE4*gross_pay
    elif gross_pay >= 3500:
        tax = RATE3*gross_pay
    elif gross_pay >1000:
        tax = RATE2*gross_pay
    else:
        tax = RATE1*gross_pay
        
    return tax

# COMPUTE FICA SOCIAL SECURITY
def compute_fica_ss(gross_pay):
    return FICA_SS*gross_pay

# COMPUTE FICA MEDICARE
def compute_medicare(gross_pay):
    return FICA_MEDICARE * gross_pay

# COMPUTE TOTAL DEDUCTIONS
def compute_tot_deduc(tax, fica_ss, fica_medicare, ins_pre, other_deduc):
    return tax + fica_ss + fica_medicare + ins_pre +other_deduc

# COMPUTE NET PAY
def compute_net_pay(gross_pay, total_deduc):
    return gross_pay - total_deduc

# PRINT PAYSLIP
def print_payslip(gross_pay, tax, fica_ss, fica_medicare, ins_prem, other_deduc,total_deductions, net_pay):
    print()
    print(f'{"Payslip":^40}')
    print()
    print(f'Gross pay:                 ${gross_pay:,.2f}')
    print()
    print(f'{"Deductions":^40}')
    print(f'Tax:                       ${tax:,.2f}')
    print(f'FICA Social Security:      ${fica_ss:,.2f}')
    print(f'FICA Medicare:             ${fica_medicare:,.2f}')
    print(f'Health Insurance Premium:  ${ins_prem:,.2f}')
    print(f'Other Deductions:          ${other_deduc:,.2f}')
    print()
    print(f'Total Deductions:          ${total_deductions:,.2f}')
    print(f'Net Pay:                   ${net_pay:,.2f}')

def main():
    gross_pay, ins_prem, other_deduc = get_input()
    tax = compute_tax(gross_pay)
    fica_ss = compute_fica_ss(gross_pay)
    fica_medicare = compute_medicare(gross_pay)
    total_deduc = compute_tot_deduc(tax, fica_ss, fica_medicare, ins_prem, other_deduc)
    net_pay = compute_net_pay(gross_pay, total_deduc)
    print_payslip(gross_pay, tax, fica_ss, fica_medicare, ins_prem, other_deduc,total_deduc,net_pay )

main()

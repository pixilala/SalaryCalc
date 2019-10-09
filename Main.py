#!/usr/bin/python3

#salaried = input('Are you on a yearly salary?: ')
#taxCode = input('What is your current Tax Code: ')
#pension = input('What is your current pension Contribution %')
################################
############TEST PARAMETERS##########
salaried = 'YES' # test parameter
taxCode = '1185L' # test parameter
hoursPerWeek = 37.5
hourlyRate = 8.7
pensionPercent = 3
studentLoanPlan = 'A'
###################################

if salaried == 'YES':
   # overHourlyRate = input('Enter hourly rate: ')
    #salaryGrossPay = input('Enter Salary: ')
    #hoursPerWeek = input('Enter Weekly Hours: ')
    salaryGrossPay = 19000
    hoursPerWeek = 37.5
    print(salaryGrossPay)
    grossSalary = salaryGrossPay
else:
    #hoursPerWeek = input('Enter Weekly Hours: ')
    #hourlyRate = input('Enter Hourly Rate: ')
    weeklyPay = float(hoursPerWeek) *  float(hourlyRate) 
    print('weekly gross pre tax: £'+ str(round(weeklyPay,2))+'0')
    nonSalarygrossPay = 13 * float(weeklyPay)
    print('Yearly gross pre tax: £'+ str(round(nonSalarygrossPay,2))+'0')
    grossSalary = nonSalarygrossPay

####
#Tax Calculations
########

if taxCode == 'BR':
    print('You are using an emergency tax code')
    taxRate = 20
    print('Tax Rate is '+str(taxRate)+' on all income')
    taxFreeAllowance = 0
elif taxCode == 'D0':
    taxRate = 40
    print('Tax Rate is '+str(taxRate)+' on all income')
    taxFreeAllowance = 0
elif taxCode == 'D1':
    taxRate = 45
    print('Tax Rate is '+str(taxRate)+' on all income')
    taxFreeAllowance = 0
elif taxCode == 'NT':
    print('You are using a Tax Free Tax Code')
    taxRate = 0
else:
    print('You Are using a personal allowance code')
    taxCodeStr = taxCode[:-1] # the [:-1] removes the last character from the string
    taxCodeAlpha = str(taxCode[-1:])
    #print(taxCodeAlpha)
personalCodes = ['L','l','P','p','Y','y','M','m','N','n','T','t']
if taxCodeAlpha in personalCodes:
    print('Personal Code')
else:
    print('check code'
          )
    taxCodeAllowance = int(taxCodeStr)
    print('Your Tax Free Allowance is: £' + str(taxCodeAllowance)+'0')
    taxFreeAllowance = taxCodeAllowance

#######
#DEDUCTIONS
###########

penContribAmount = ((int(pensionPercent) / 100) * int(grossSalary)/12)
penContrib=(round(penContribAmount,2))
print('Current pension contributions are: ' + str(penContrib))
grossSalaryInt = int(grossSalary)

######
#Student Loan Calc
#########

if studentLoanPlan == 'A':
    if grossSalaryInt > 18935:
        studentLoanDeductionPercentage = 0
        SLDeductionAmount = grossSalaryInt
    else:
        studentLoanDecuctionPercentage = 9
        SLDeductionAmount = ((grossSalaryInt / 100) * studentLoanDecuctionPercentage)/12
        print(SLDeductionAmount)
    print('A')

elif studentLoanPlan == 'B':
    if grossSalaryint > 25725:
        studentLoanDeductionPercentage = 0
    else:
        studentLoanDecuctionPercentage = 9
        SLDeductionAmount = ((grossSalaryInt / 100) * studentLoanDecuctionPercentage)/12
        print(SLDeductionAmount)
    print('B')
else:
    if grossSalaryint > 21000:
        studentLoanDeductionPercentage = 0
    else:
        studentLoanDeductionPercentage = 6
        SLDeductionAmount = ((grossSalaryInt / 100) * studentLoanDecuctionPercentage)/12
        print(SLDeductionAmount)
    print('Sudent Loan')

######
#N.I Calcs
#########
grossWeeklyPay = ((grossSalaryInt / 12)/4)
if grossWeeklyPay <= 166:
    NIPercent = 0
elif grossWeeklyPay >=166 and grossWeeklyPay <= 962:
    NIPercent = 12
print(NIPercent)

#####
#Tax Calculation
########
if grossSalaryInt <= 12500:
                 taxRate = 0.00
                 print('You have not reached your monthly allowance')
elif grossSalaryInt >= 12501 and grossSalaryInt < 50000:
                 taxRate = 0.20
                 print('You are on Basic Rate (20%)')
elif grossSalaryInt >= 50001 and grossSalaryInt < 150000:
                 taxRate = 0.40
                 print('You are on Higher Rate Tax (40%)')
elif grossSalaryInt >= 150000:
                 taxRate = 0.45
                 print('You are on Additonal Rate Tax (45%)')

if taxCodeStr == 'BR':
    deductableAmount = grossSalaryInt
    print(deductableAmount)
else:
    deductableAmount = grossSalaryInt * taxRate
    print('Deductable Amount £'+str(float(round(deductableAmount,2)))+'0')

totalNetSalary = grossSalaryInt - deductableAmount
monthlyNetSalary = totalNetSalary / 12

#### end salary calculation
if salaried == 'YES':
    print('Your Total Net Salary: £'+str(float(round(monthlyNetSalary,2))))
else:
    print('Your Total Net Salary: £'+str(float(round(totalNetSalary,2))))

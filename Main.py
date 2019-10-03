#!/usr/bin/python3

#salaried = input('Are you on a yearly salary?: ')
#taxCode = input('What is your current Tax Code: ')
salaried = 'no' # test parameter
taxCode = '1185l' # test parameter
hoursPerWeek = 50
hourlyRate = 8.7

if salaried == 'YES':
   # overHourlyRate = input('Enter hourly rate: ')
    salaryGrossPay = input('Enter Salary: ')
    hoursPerWeek = input('Enter Weekly Hours: ')
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

if taxCode == 'BR':
                 print('You are using an emergency tax code')
                 taxCodeStr = 'BR'
else:
                 print('You Are using a personal allowance code')
                 taxCodeStr = taxCode[:-1] # the [:-1] removes the last character from the string
                 #print(taxCodeStr)
                 taxCodeAllowance = int(taxCodeStr)
                 print('Your Tax Free Allowance is: £' + str(taxCodeAllowance)+'0')

if taxCodeStr == 'BR':
                taxFreeAllowance = 0
else:
                taxFreeAllowance = taxCodeAllowance
#
grossSalaryInt = int(grossSalary)

#taxcalculation
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
    print('Your Total Net Salary: £'+str())

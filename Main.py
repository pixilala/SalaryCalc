#!/usr/bin/python3

salaried = input('Are you on a yearly salary?: ')

if salaried == True:
    overHourlyRate = input('Enter hourly rate: ')
    salary = input('Enter Salary: ')
    hoursPerWeek = input('Enter Weekly Hours :')
else:
    hoursPerWeek = input('Enter Weekly Hours: ')
    hourlyRate = input('Enter Hourly Rate: ')
    payPeriodsPerYear = input('How Many Pay Periods Per Year :')
    print(hoursPerWeek)
    weeklyPay = 4.0 * float(hoursPerWeek)  
    print('weekly salary pre tax: '+ str(weeklyPay))
    Salary = float(weeklyPay) * float(payPeriodsPerYear)
    print('Yearly salary pre tax: '+ str(Salary))
#hourlyRate = float(salary) / 52 / float(hoursPerWeek)
#print(hourlyRate)

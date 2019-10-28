#!/usr/bin/python3

def calculate_weekly_from_salary(salary, monthly):
#sometimes you get paid every 4 weeks not once a month
	if (monthly):
		per_month = salary / 12
	else:
		per_month = salary / 13
	return per_month/4

def calculate_hourly_rate(salary, hours_in_working_week):
	hours_worked = hours_in_working_week*48
	return salary/hours_worked

def calculate_pension_contributions(salary, contribution_percent):
	return salary * (contribution_percent/100)

def calculate_weekly_pension_contributions(salary, contribution_percent):
	return calculate_pension_contributions(salary, contribution_percent)/48

def print_info(wage_params, deductions):
	weekly = calculate_weekly_from_salary(wage_params[0], wage_params[2])
	hourly = calculate_hourly_rate(wage_params[0], wage_params[1])
	if (deductions):
		print("with deductions:\n")
		weekly = weekly - calculate_weekly_pension_contributions(wage_params[0], 3)
	else:
		print("without deductions:")

	print("you earn {0} a week\n and {1} an hour ".format(weekly, hourly))

def main():
	wage_params = []
	salary = float(input("\nenter salary: "))
	weekly_hours = float(input("enter weekly hours: "))
	monthly = bool(input("are you paid monthly as opposed to every 4 weeks: "))
	wage_params.append(salary)
	wage_params.append(weekly_hours)
	wage_params.append(monthly)

	print(wage_params)

	print_info(wage_params, bool(input("show deductions: ")))

if __name__ == "__main__":
	main()

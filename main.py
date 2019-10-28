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

def main():
	salary = float(input("\nenter salary: "))
	weekly_hours = float(input("enter weekly hours: "))
	monthly = bool(input("are you paid monthly as opposed to every 4 weeks: "))

	print("hourly rate is:{0}".format(calculate_hourly_rate(salary, weekly_hours)))
	print("you get {0} a week".format(calculate_weekly_from_salary(salary, monthly)))

if __name__ == "__main__":
	main()

import sys
import numpy


def simulate_savings(percentage_saved: int, starting_salary: int) -> int:
	current_savings = 0
	return_rate = .04/12
	monthly_salary = (starting_salary * percentage_saved) / 12
	salary_increase = .07
	for month in range (1, 37):
		current_savings += monthly_salary + (current_savings * return_rate)
		if month % 6 == 0:
			starting_salary += salary_increase * starting_salary
			monthly_salary = percentage_saved * (starting_salary/12)
	return current_savings

def bisection_search(salary: int, down_payment: int):
	epsilon = 100
	search_count = 1
	low = 1
	high = 10000
	if simulate_savings(1, salary) < down_payment:
		return -1

	while low <= high:
		guess = (low + high) // 2
		percentage_of_salary_saved = guess / 10000
		if abs(down_payment - simulate_savings(percentage_of_salary_saved, salary)) <= epsilon:
			return (search_count, percentage_of_salary_saved)
		elif simulate_savings(percentage_of_salary_saved, salary) < down_payment:
			low = guess + 1
			search_count += 1
		else:
			high = guess - 1
			search_count += 1
	return (search_count, percentage_of_salary_saved)
			
			
		
		

	







def main():

	
	house_cost = 1000000
	down_payment_needed = house_cost * .25


	print('Hello I will calculate how many months it will take you to save up money for a down payment!')
	starting_salary = float(input('Please enter your annual salary: '))
	

	steps = bisection_search(starting_salary, down_payment_needed)
	if steps == -1:
		print('It is not possible to pay the down payment in three years')
	else:
		print(f"Steps in the bisection search is {steps[0]} {steps[1]}")

	





if __name__ == '__main__':
	main()
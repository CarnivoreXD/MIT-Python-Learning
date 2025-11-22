import sys
import numpy





def main():

	portion_down_payment = .25
	current_savings = 0
	return_rate = .04
	monthly_return_rate = return_rate / 12
	number_of_months = 0

	print('Hello I will calculate how many months it will take you to save up money for a down payment!')
	annual_salary = float(input('Please enter your annual salary:'))
	portion_saved = float(input('Please enter the portion of your salary to be saved in decimal notation:'))
	total_cost = float(input('Please enter your dream homes price:'))

	monthly_salary = portion_saved * (annual_salary/12)
	down_payment_needed = total_cost * portion_down_payment

	while(current_savings < down_payment_needed):

		current_savings += monthly_salary + (current_savings * monthly_return_rate) 
		number_of_months += 1

	print(f"The number of months it will take to save {down_payment_needed}  is  {number_of_months}")

	





if __name__ == '__main__':
	main()
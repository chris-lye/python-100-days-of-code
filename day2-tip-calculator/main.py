#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total_bill = float(input("How much was the total bill?\n"))
tip_percentage = int(input("How much percentage tip do you want to give? (e.g. 10, 12 or 15)\n"))
people = int(input("How many people are splitting the bill?\n"))

final_bill = total_bill + (tip_percentage / 100 * total_bill) # normally, you would avoid dividing a possible 0 value by any number
individual_bill = round(final_bill / people, 2)

individual_bill = format(individual_bill, '.2f') # forces results such as 15.1 to become 15.10

print(f"Each person should pay ${individual_bill}")
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip = int(input("How much would you like to tip? (10, 12 or 15 percent) "))/100
people = int(input("How many people to split the bill? "))

split = (total_bill * (1 + tip)) / people

# First time using formating, found details here: https://realpython.com/python-numbers/
# : indicates everything after this is formating
# .2 means up to 2 decimal places
# f means fixed decimal places, so it would show $20.10 with the f  and $20.1 without it
print(f"Each person should pay: ${split:.2f}")

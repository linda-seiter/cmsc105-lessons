"""
This program prompts for the total bill, tip percentage, and number of people splitting the bill,
then calculates and shows the tip, total bill, and cost per person, each formatted to two decimal places.

Author: First Last
Date: January 1, 2025
Version: 1.0
"""

# TODO: Prompt for total bill, tip percentage, and number of people
bill = float(input("Total bill: $"))
tip = int(input("Tip Percentage (ex. 10 12 15): "))
people = int(input("How many people: "))

# TODO: Calculate total tip, total bill, and amount per person
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
amount_per_person = total_bill / people

# TODO: Print total tip, total bill, amount per person, formatted to 2 decimal places
print(f'Total tip: ${total_tip:.2f}')
print(f'Total_bill: ${total_bill:.2f}')
print(f'Amount per person: ${amount_per_person:.2f}')



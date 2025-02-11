"""
This program prompts for the price and tip percentage, then calculates and shows the tip amount, formatted to two decimal places.

Author: First Last
Date: January 1, 2025
Version: 1.0
"""

# Prompting for input
price = float(input('Price: '))
tip_percent = int(input('Tip %: '))

#Calculating the tip based on price and percentage
tip = price * tip_percent / 100  # Assuming the tip percent is entered as a percentage (e.g., 20 for 20%)

#Displaying the result formatted to 2 decimal places
print(f'The tip should be ${tip:.2f}.')
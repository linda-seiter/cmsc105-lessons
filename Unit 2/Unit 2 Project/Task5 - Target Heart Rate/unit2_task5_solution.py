"""
This program prompts for the age, then calculates
and displays the maximum heart rate along with a
range for moderate and intense activity.

Author: First Last
Date: January 1, 2025
Version: 1.0
"""

import math

# TODO: Prompt for age
age = int(input("Please enter your age in years: "))

# TODO: Calculate maximum rate, 50%, 70%, and and 85%, rounded down to nearest integer
max_rate = 220 - age
rate_50_percent = math.floor(max_rate * 0.50)
rate_70_percent = math.floor(max_rate * 0.70)
rate_85_percent = math.floor(max_rate * 0.85)

# TODO: Display the result
print(f'For Age = {age} years,')
print(f'Maximum heart rate = {max_rate} bpm')
print(f'Target for moderate activity = {rate_50_percent} to {rate_70_percent} bpm')
print(f'Target for intense activity = {rate_70_percent} to {rate_85_percent} bpm')
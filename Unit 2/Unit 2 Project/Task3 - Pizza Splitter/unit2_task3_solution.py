"""
This program prompts for the number of slices and people, then calculates and displays the slices per person and any leftover slices.

Author: First Last
Date: January 1, 2025
Version: 1.0
"""


#  TODO: Prompt for number of slices and people
slices = int(input('How many slices: '))
people = int(input('How many people: '))

# TODO: Calculate the slices per person and leftover slices
slices_per_person = slices // people
leftover_slices = slices % people

# TODO: Display the slices per person and leftover slices
print(f'Each person gets {slices_per_person} slices.')
print(f'There are {leftover_slices} slices leftover.')
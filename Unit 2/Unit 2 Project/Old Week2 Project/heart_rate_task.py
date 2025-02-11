age = int(input("Please enter your age in years: "))

max_rate = 220 - age
rate_50_percent = max_rate * 0.50
rate_70_percent = max_rate * 0.70
rate_85_percent = max_rate * 0.85

print(f'For Age = {age} years,')
print(f'Maximum heart rate = {max_rate} bpm')
print(f'Target Heart Rate for moderate activity = {rate_50_percent} to {rate_70_percent} bpm')
print(f'Target Heart Rate for intense activity = {rate_70_percent} to {rate_85_percent} bpm')


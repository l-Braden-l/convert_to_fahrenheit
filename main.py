# Braden Leach
#December 11 2024 
#Convert to fahrenheit project



import time 
#----Convert to fahrenheit----#

for num in range(0,21):
    fahrenheit = num * (9/5) + 32
    print(f'Celsius: {num}°C   Fahrenheit: {fahrenheit:.1f}°F')
    time.sleep(1)
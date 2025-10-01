'''8. Temperature Converter
	•	Ask user for temperature in Celsius or Fahrenheit.
	•	Convert to the other scale.
	•	Print the result.'''

result = 0
print("This is a converter for degrees Celsius and Fahrenheit. You can enter which one you'd like to convert from.")
unit = input("Enter the unit you want to convert FROM (use 'C' or 'F' ): ").upper()
while True:
    if not unit in ["C", "F"]:
        unit = input("Invalid selection. Enter 'C' or 'F'. ").upper()
    else: break
degrees = input(f"Enter the °{unit} you want to convert: ")
while True:
    try: degrees = float(degrees); break
    except: degrees = input("Invalid input. Enter a number. ")
if unit == "C":
    result = degrees * (9/5) + 32
    print(f"{degrees}°C is equal to {result}°F.")
elif unit == "F":
    result = (degrees - 32) * (5/9)
    print(f"{degrees}°F is equal to {result}°C.")
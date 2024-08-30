def convert_temperature(value, to_scale):
    if to_scale == 'C':
        return (value - 32) * 5/9
    elif to_scale == 'F':
        return (value * 9/5) + 32
    else:
        raise ValueError("Unknown scale")

value = float(input("Enter the temperature value: "))
from_scale = input("Convert from (C/F): ").upper()
to_scale = input("Convert to (C/F): ").upper()

if from_scale == to_scale:
    print(f"Value is the same: {value:.2f} {to_scale}")
else:
    converted_value = convert_temperature(value, to_scale)
    print(f"Converted value: {converted_value:.2f} {to_scale}")

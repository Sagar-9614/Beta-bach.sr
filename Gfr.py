# Function to get valid integer input
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print("Please enter a valid integer.")

# Function to get valid float input
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Please enter a valid number.")

# Get user inputs with validation
age = get_int_input('Age: ')
weight = get_float_input('Weight (kg): ')
creatinine = get_float_input('Serum Creatinine (mg/dL): ')

# Calculate GFR using Cockcroft-Gault formula
gfr = ((140 - age) * weight) / (72 * creatinine)

# Print the result
print(f"Estimated GFR: {gfr:.2f} mL/min")
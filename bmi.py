# BMI Calculator Program

# Step 1: Take input from user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Step 2: Calculate BMI
bmi = weight / (height ** 2)

# Step 3: Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Step 4: Display result
print("\n--- BMI RESULT ---")
print("Your BMI is:", round(bmi, 2))
print("BMI Category:", category)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")

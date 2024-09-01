print("BMI Calculator")
weight = float(input("What is your weight in kilograms:?: "))
height = float(input("What is your height in meters:? "))

bmi = weight / pow(height, 2)

if bmi <= 18.4:
    print("You are underweight.")
elif bmi >=18.4 and bmi <= 24.9:
    print("You are in the normal range.")
elif bmi >= 25.0 and bmi <= 39.9:
    print ("You are overweight.")
elif bmi >= 40:
    print("You are obese.")
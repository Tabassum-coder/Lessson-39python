#BMI checker

height=int(input("Enter height in cms"))
weight=int(input("Enter weight in kg"))

bmi=weight/(height/100)**2

if bmi<=18.4:
    print("You are underweight")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are over weight")
elif bmi<=34.9:
    print("You are severely over weight")
elif bmi<=39.9:
    print("You are obese")
else:
    print("You are severely obese")

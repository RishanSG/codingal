x=float(input("Height in m : "))
y=float(input("Weight in kilograms : "))
x2=x**2
z=y/x2
if z<=18.5:
    print(f"The person has {z} BMI and is Thin")
elif 18.6<=z<=24.9:
    print(f"Person has {z} BMI and is Healthy")

elif 25<=z<=29.9:
    print(f"person has {z} BMI and is Overweight")
elif z<=30:
    print(f"Person has {z} BMI and is Obese")

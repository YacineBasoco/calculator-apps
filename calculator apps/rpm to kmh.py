import matplotlib.pyplot as plt
import math

def repeat():
    while True:
        try:
            repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
            if repeat == 'yes':
                return True
            elif repeat == 'no':
                return False
            else:
                print("Invalid input, please choose between 'yes' and 'no'.")
        except TypeError:
            print("Error: Invalid input, please choose between 'yes' and 'no'.")

while True:
    diameter_model = float(input("Diameter (mm)= ")) / 1000
    if diameter_model <= 0:
        print("Error, the fan's diameter must be a number above 0.")
        continue
    else:
        break
scale = 5/diameter_model
diameter_real = diameter_model * scale
while True:
    EF = float(input("Efficiency factor = "))
    if EF <= 0 or EF >= 1:
        print("Error: Efficiency factor must be between 0 and 1.")
        continue
    else:
        break
while True:
    frontal_area = float(input("Area of the model's frontal area (cm²) = ")) * (scale**2) / 10000
    if frontal_area <= 0:
        print("Error, the vehicle's frontal area must be a number above 0.")
        continue
    else:
        break
while True:
    mass_model = float(input("Model's mass (g) = ")) / 1000
    if mass_model <= 0:
        print("Error, the model's mass must be a number above 0.")
        continue
    else:
        break
while True:
    tilt = float(input("Degrees of tilt in the string = "))
    if tilt < 0:
        print("Error, the string's tilt must be a positive number.")
        continue
    else:
        break


while True:
    try:
        kmh_list = [0]
        rpm_list = [0]

        rpm_count = int(input("How many rpm do you want to input?\n"))
        if rpm_count <= 0:
            print("Error: Please enter a number above 0.")
            continue

        if rpm_count > 1:
            kmh_list.remove(0)
            rpm_list.remove(0)

        for i in range(rpm_count):
            rpm_model = int(input(f"rpm #{i + 1} = "))
            rpm = rpm_model / math.sqrt(scale)

            rpm_list.append(round(rpm))
            kmh = round((((rpm * math.pi * diameter_real) / 60) * EF) * 3.6, 2)
            kmh_list.append(kmh)

        print(f'\nrpm = {rpm_list}')
        print(f"km/h = {kmh_list}")
        print(f"1:{scale:.1f}")

        plt.plot(rpm_list, kmh_list, color='red')
        plt.title("Speed of the Airflow")
        plt.xlabel("rpm")
        plt.ylabel("Speed (km/h)")
        plt.grid(True)
        plt.show()

    except ValueError:
        print("Invalid input, please enter numbers only.")
        continue

    if not repeat():
        break

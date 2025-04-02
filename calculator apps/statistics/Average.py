def repeat():
    repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
    if repeat == 'yes':
        return True
    elif repeat == 'no':
        return False
    else:
        print("Invalid input, please choose between yes and no.")
        return repeat()

def average():
    while True:
        try:
            a = int(input("How many numbers do you want to input?\n"))

            values = []
            for i in range(a):
                value = float(input(f"Enter the number {i+1} of your list: "))
                values.append(value)

            total = sum(values)

            average = (total)/a
            print(values)
            print(total)
            print(f"average : {average:.2f}")

        except ValueError or TypeError:
            print("Error: Invalid input, please input numbers only")
            continue
        if not repeat():
            break

average()
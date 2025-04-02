def repeat():
    repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
    if repeat == 'yes':
        return True
    elif repeat == 'no':
        return False
    else:
        print("Invalid input, please choose between yes and no.")
        return repeat()

def savings():
    currency = input("What currency will you be using?\n")
    while True:
        try:
            option = int(input("What do you want to calculate?\n1. Time until you've reached your goal\n2. Money needed to reach your goal in a certain amount of time\n"))
            if option == 1:
                days = 0
                total = float(input("How much money do you need in total?\n"))
                savings = float(input("How much money are you starting with?\n"))
                add = float(input("How much are you adding per day?\n"))

                while savings < total:
                    days += 1
                    savings += add


                if days >= 365:
                    years = days / 365
                    if years > 1:
                        print(f"You will need approximately {years:.2f} years or {days:,} days to reach your goal.")
                    else:
                        print(f"You will need one year to reach your goal.")

                elif days >= 30:
                    months = days / 30
                    if months > 1:
                        print(f"You will need approximately {months:.2f} months or {days:,} days to reach your goal.")
                    else:
                        print(f"You will need one month to reach your goal.")

                elif days >= 7:
                    weeks = days / 7
                    if weeks > 1:
                        print(f"You will need approximately {weeks:.2f} weeks or {days:,} days to reach your goal.")
                    else:
                        print(f"You will need one week to reach your goal.")

                else:
                    if days >= 1:
                        print(f"You will need {days} days to reach your final budget.")
                    else:
                        print(f"You will need one day to reach your final budget.")
            elif option ==2:
                while True:
                    time_unit = input("Will you be using days, months, or years? ").lower().strip()

                    if time_unit == 'days':
                        word = 'day'
                        multiplier = 1
                        break
                    elif time_unit == 'months':
                        word = 'month'
                        multiplier = 30
                        break
                    elif time_unit == 'years':
                        word = 'year'
                        multiplier = 365
                        break
                    else:
                        print("Error: invalid input, please enter either 'days', 'months', or 'years'.")

                total = float(input("How much money do you need in total?\n"))
                savings = float(input("How much money are you starting with?\n"))
                finish_line = float(input(f"In how many {word} do you need {total:.0f}{currency}?\n"))*multiplier

                if finish_line <= 0:
                    print("Error: The time period must be greater than 0.")
                else:
                    add = (total - savings) / finish_line
                    print(f"You need to save {add:.2f} per {word} to reach your goal.")


        except (ValueError or TypeError):
            print("Error: Invalid input, please input numbers only")
            continue
        if not repeat():
            break

savings()
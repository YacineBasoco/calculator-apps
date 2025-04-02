import time

def repeat():
    repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
    if repeat == 'yes':
        return True
    elif repeat == 'no':
        return False
    else:
        print("Invalid input, please choose between yes and no.")
        return repeat()

def statistics():
    currency = input("What currency will you be using?\n")
    while True:
        try:
            choice4 = int(input("What do you want to calculate?\n1. Interest growth\n2. Loan return\n3. Investments\n4. Average\n"))
            if choice4 == 1:

                years = int(input("For how many years will you be investing?\n"))
                a = float(input(f"Initial price (in {currency}): "))
                b = float(input(f"Monthly addition (in {currency}): "))
                c = float(input("Growth rate (in %): "))/100

                initial_investment = a+(b*12*years)

                for i in range(1, years+1):
                    a = a * (1+c/12)**12
                    for _ in range(12):
                        a += b*(1+c/12)**(12 - _)
                    print(f"Year {i}: {currency}{a:,.0f}")
                    time.sleep(0.01)

                total_growth = a - initial_investment
                percentage_growth = (total_growth * 100)/a
                print(f"\nAfter {years} years, you will have {a:,.0f}{currency}")
                print(f"Which is {total_growth:,.0f}{currency} more than the amount you invested")
                print(f"Which means a total of {percentage_growth:.2f}% more\n\n")
                time.sleep(8)
            elif choice4 == 2:

                years = float(input("Loan duration (in years): "))
                principal = float(input(f"Loan amount (in {currency}): "))
                monthly_rate = float(input("Monthly interest rate (in %): "))/100

                total_months = years*12

                if monthly_rate == 0:
                    monthly_payment = principal/total_months
                else:
                    monthly_payment = (
                        principal*monthly_rate*(1+monthly_rate)**total_months
                    ) / ((1 + monthly_rate) ** total_months - 1)

                print(f"\nFor a loan of {principal:,.0f}{currency} at {monthly_rate * 100:,.2f}% monthly interest:")
                print(f"Over {years:,.2f} years, you need to pay back {monthly_payment:,.2f}{currency} per month\n\n")
                time.sleep(8)
            elif choice4 == 3:
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
            elif choice4 == 4:
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
            else:
                print("Invalid input. Please type '1' or '2'.")
                continue


        except ValueError or TypeError:
            print("Invalid input, please enter numbers only.")
            continue
        if not repeat():
            break

statistics()
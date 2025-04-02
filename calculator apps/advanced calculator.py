from sympy import symbols, Eq, solve, solve_univariate_inequality, expand, factor, sympify, Rational, pprint
import matplotlib.pyplot as plt
import re, math, time

def repeat():
    while True:
        try:
            repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
            if repeat == 'yes':
                return True
            elif repeat == 'no':
                break
            else:
                print("Invalid input, please choose between 'yes' and 'no'.")
                continue
        except TypeError:
            print("Error: Invalid input, please choose between 'yes' and 'no'.")
            continue

def algebra():
    while True:
        try:
            choice3 = int(input("Choose between:\n1. Equations\n2. Inequations\n3. Factorize\n4. Functions\n"))

            x = symbols('x')
            def process_input(user_input):
                user_input = user_input.replace('^', '**').replace(' ', '')
                user_input = re.sub(r'(?<=\d)(?=x)', '*', user_input)
                user_input = re.sub(r'(?<=\d)(?=\()', '*', user_input)
                user_input = re.sub(r'(?<=\))(?=\()', '*', user_input)
                return user_input
            def format_output(expr):
                superscript_digits = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
                formatted = str(expr)
                formatted = formatted.replace('*x', 'x').replace('1x', 'x').replace('sqrt', '√')
                formatted = re.sub(r'\*\*(\d+)', lambda match: ''.join(superscript_digits[digit] for digit in match.group(1)), formatted)
                return formatted


            if choice3 == 1:
                type_of_equation = int(input("What type of equation do you want to solve?\n1. Develop a factorized equation\n2. Resolve an equations\n"))

                if type_of_equation == 1:
                    expr_input = input("Enter an expression to expand: (e.g., (5x +6)^2 ): ").strip().lower()
                    expr_input = process_input(expr_input)

                    try:
                        expr = sympify(expr_input)
                    except Exception as e:
                        print(f"Error in parsing the expression: {e}")
                        continue

                    result = expand(expr)
                    print(f"{expr_input} expanded is {format_output(result)}")
                elif type_of_equation == 2:
                    equation_input = input("Enter an equation to solve: (e.g., (5x+6)^2 - (x-9)^2 = 0 ): ").strip().lower()
                    equation_input = process_input(equation_input)

                    if '=' not in equation_input:
                        print("Error: Please enter a valid equation with '=' sign.")
                        return

                    try:
                        left_side, right_side = equation_input.split('=')
                        left_expr = sympify(left_side)
                        right_expr = sympify(right_side)

                        equation = Eq(left_expr, right_expr)
                        solutions = solve(equation, x)

                        print(f"Equation: {format_output(equation)}")
                        print(f"Solutions: {solutions}\n")
                    except Exception as e:
                        print(f"Error in solving the equation: {e}")
                        continue
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    continue
            elif choice3 == 2:
                inequality_input = input("Enter an inequality to solve: (e.g., (x-9)^2 <= 36 ): ").strip().lower()
                inequality_input = process_input(inequality_input)

                if '>' not in inequality_input and '<' not in inequality_input and '>=' not in inequality_input and '<=' not in inequality_input:
                    print("Error: Please enter a valid inequality with a comparison operator (>, <, >=, <=).")
                    return

                try:
                    inequality_expr = sympify(inequality_input)
                    solution = solve_univariate_inequality(inequality_expr, x)

                    print(f"Inequality: {format_output(inequality_expr)}")
                    print(f"Solution: {solution}\n")

                except Exception as e:
                    print(f"Error in solving the inequality: {e}")
                    continue
            elif choice3 == 3:

                expr_input = input("Enter an expression to factorize: (e.g., 25x^2 +60x +36 ): ").strip().lower()
                expr_input = process_input(expr_input)

                try:
                    expr = sympify(expr_input)
                except Exception as e:
                    print(f"Error in parsing the expression: {e}")
                    continue

                result = factor(expr)
                print(f"{expr_input} factorized is {format_output(result)}")
            elif choice3 == 4:
                choice = int(input("Choose between:\n1. Draw a function\n2. Find a linear function's formula\n"))
                if choice == 1:
                    while True:
                        function_input = input("Enter the function's formula: (e.g., sqrt(x) + 1/x + x^2 - 4x ): ").lower().strip()
                        processed_function = process_input(function_input)
                        try:
                            expr = sympify(processed_function)
                            break
                        except Exception:
                            print("Error: Invalid function, please enter a correct mathematical expression")
                            continue

                    function_define = input("Enter the function's range: (e.g., 1, 10 ): ").strip().lower()
                    try:
                        range_values = [int(i.strip()) for i in function_define.split(',')]
                        if len(range_values) != 2 or range_values[0] >= range_values[1]:
                            raise ValueError
                    except (ValueError, TypeError):
                        print("Error: Invalid range, please enter a valid range like '-10, 10'.")
                        continue

                    if 'sqrt(x)' in function_input and range_values[0] < 0:
                        print("Error: sqrt(x) is undefined for negative values in the given range.")
                        continue

                    x_values = [i for i in range(range_values[0], range_values[1] + 1) if not (expr == 1/x and i == 0)]
                    y_values = [expr.subs(x, val) for val in x_values]

                    plt.plot(x_values, y_values, label=f"f(x) = {function_input}", color='red')
                    plt.title(f"Graph of f(x) = {format_output(expr)}")
                    plt.xlabel("x")
                    plt.ylabel("f(x)")
                    plt.grid(True)
                    plt.show()

                    x_values = list(range(range_values[0], range_values[1] + 1))
                    y_values = [expr.subs(x, value) for value in x_values]

                    def value(x_values, y_values):
                        print(f"\nValue table of f(x) = {format_output(expr)}")
                        print(f"{'x':<5}| {'f(x)':<10}")
                        print("-" * 20)

                        for x, y in zip(x_values, y_values):
                            y_val = round(y.evalf(), 2) if hasattr(y, 'evalf') else round(y, 2)
                            print(f"{x} | {y_val}")

                    value(x_values, y_values)
                elif choice == 2:
                    x = symbols('x')

                    f0 = Rational(input('f(0) = '))
                    f1 = Rational(input('f(1) = '))

                    a = (f0 - f1) / (0 - 1)
                    b = f1 - a*1

                    print("Equation: f(x) = ax + b")
                    pprint(f"f(x) =  {a*x + b}")
                else:
                    print("Error: Invalid input, please choose a valid option.")
            else:
                print("Error: Invalid input, please choose a valid option.")
                continue

        except (ValueError, TypeError):
            print("Error, Invalid input, please enter an integer.")
            continue
        if not repeat():
            break
def advanced_math():
    while True:
        try:
            choice5 = int(input("Choose between:\n1. Calculus\n2. Multivariable Calculus\n3. Finantial Mathematics\n"))
            if choice5 == 1:
                choice = int(input("Choose between:\n1. Derivatives\n2. Intergrals\n3. Differentials\n4. Series and sequences"))

                if choice == 1:
                    print("idk calculus yet")
                elif choice == 2:
                    print("idk calculus yet")
                elif choice == 3:
                    print("idk calculus yet")
                elif choice == 4:
                    print("idk calculus yet")
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    return
            elif choice5 == 2:
                choice = int(input("Choose between:\n1. Partial Derivatives\n2. Multipal Intergrals\n3. Gradient, Divergence, and Curl\n4. Line and Surface Integrals"))

                if choice == 1:
                    print("idk multicalculus yet")
                elif choice == 2:
                    print("idk multicalculus yet")
                elif choice == 3:
                    print("idk multicalculus yet")
                elif choice == 4:
                    print("idk multicalculus yet")
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    return
            elif choice5 == 3:
                currency = input("What currency will you be using?\n")
                choice = int(input("Choose between:\n1. Compound interest growth\n2. Interest growth\n3. Loan amortization schedule\n4. Morgage amortization schedule"))
                if choice == 1:
                    print("i still don't know advanced math")
                elif choice == 2:
                    years = int(input("For how many years will you be investing?\n"))
                    a = float(input(f"Initial price (in {currency}): "))
                    b = float(input(f"Monthly addition (in {currency}): "))
                    c = float(input("Growth rate (in %): "))/100

                    initial_investment = a+(b*12*years)

                    for i in range(1, years+1):
                        a = a * (1+c/12)**12
                        for month in range(1, 13):
                            a += b*(1+c/12)**(12 - month)
                        print(f"Year {i}: {currency}{a:,.0f}")
                        time.sleep(0.01)

                    total_growth = a - initial_investment
                    percentage_growth = (total_growth * 100)/a
                    print(f"\nAfter {years} years, you will have {a:,.0f}{currency}\nWhich is {total_growth:,.0f}{currency} more than the amount you invested\nWhich means a total of {percentage_growth:.2f}% more\n\n")
                    time.sleep(8)
                elif choice == 3:
                    years = float(input("Loan duration (in years): "))
                    principal = float(input(f"Loan amount (in {currency}): "))
                    monthly_rate = float(input("Monthly interest rate (in %): "))/100

                    total_months = years*12

                    if monthly_rate == 0:
                        monthly_payment = principal/total_months
                    else:
                        monthly_payment = (principal*monthly_rate*(1+monthly_rate)**total_months) / ((1 + monthly_rate) ** total_months - 1)

                    print(f"\nFor a loan of {principal:,.0f}{currency} at {monthly_rate * 100:,.2f}% monthly interest:")
                    print(f"Over {years:,.2f} years, you need to pay back {monthly_payment:,.2f}{currency} per month\n\n")

                    remaining_balance = principal
                    for month in range(1, int(total_months)+1):
                        interest_paid = remaining_balance*monthly_rate
                        principal_paid = monthly_payment - interest_paid
                        remaining_balance -= principal_paid

                        print(f"Month {month}:\n- Interest paid = {interest_paid:,.2f}{currency}\n- Principal paid = {principal_paid:,.2f}{currency}\n- Remaining balance = {remaining_balance:,.2f}{currency}\n")
                        time.sleep(0.01)
                elif choice == 4:
                    print("i still don't know advanced math")
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    continue
            else:
                print("Error: Invalid input, please choose a valid option")
                return

        except (ValueError, TypeError):
            print("Error, Invalid input, please enter an integer.")
            continue
        if not repeat():
            break

def main():
    while True:
        try:
            section = int(input("Choose between:\n1. Algebra\n2. Advanced math\n"))

            if section == 1:
                algebra()
                break
            elif section == 2:
                advanced_math()
                break
            else:
                print("Error: Invalid input, please enter either '1', '2', '3' or '4'.")
                continue
        except (ValueError, TypeError):
            print("Error, Invalid input, please enter an integer.")

main()
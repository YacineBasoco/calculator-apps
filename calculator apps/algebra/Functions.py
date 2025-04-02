import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, solve_univariate_inequality, expand, factor, sympify, Rational, pprint
import re

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

x = symbols('x')

def process_input(user_input):
    user_input = user_input.replace('^', '**').replace(' ', '')
    user_input = re.sub(r'(?<=\d)(?=x)', '*', user_input)
    return user_input
def format_output(expr):
    superscript_digits = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
    formatted = str(expr)
    formatted = formatted.replace('*x', 'x').replace('1x', 'x')
    formatted = re.sub(r'\*\*(\d+)', lambda match: ''.join(superscript_digits[digit] for digit in match.group(1)), formatted)
    return formatted

while True:
    try:
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
            except ValueError:
                print("Invalid range. Please enter a valid range like '-10, 10'.")
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
            print("Error: Invalid input, please enter either '1' or '2'")

    except ValueError:
        print("Invalid input, please enter numbers only.")
        continue
    if not repeat():
        break
from sympy import symbols, sympify
import re

def repeat():
    repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
    if repeat == 'yes':
        return True
    elif repeat == 'no':
        return False
    else:
        print("Invalid input, please choose between yes and no.")
        return repeat()

def tables():
    while True:
        try:
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

            function_define = input("Enter the function's range (e.g., -10, 10): ").strip().lower()
            try:
                range_values = [int(i.strip()) for i in function_define.split(',')]
                if len(range_values) != 2 or range_values[0] >= range_values[1]:
                    raise ValueError
            except ValueError:
                print("Invalid range. Please enter a valid range like '-10, 10'.")
                return

            function_input = input("Enter the function's formula (e.g., x^2 + 2x + 1): ").lower().strip()
            function_formula = process_input(function_input)

            x = symbols('x')
            try:
                expr = sympify(function_formula)
            except Exception as e:
                print(f"Invalid formula: {e}")
                return

            x_values = list(range(range_values[0], range_values[1] + 1))
            y_values = [expr.subs(x, value) for value in x_values]

            def value(x_values, y_values):
                print(f"\nValue table of f(x) = {format_output(expr)}")
                print("x  |", "  ".join(map(str, x_values)))
                print(format_output(expr), "|", "  ".join(map(str, y_values)))

            value(x_values, y_values)

        except ValueError:
            print("Invalid input, please enter numbers only.")
            continue
        if not repeat():
            break

tables()

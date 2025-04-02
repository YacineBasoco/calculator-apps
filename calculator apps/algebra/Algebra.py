from sympy import symbols, Eq, solve, solve_univariate_inequality, expand, factor, sympify
import matplotlib.pyplot as plt
import re
import math

def repeat():
    repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
    if repeat == 'yes':
        return True
    elif repeat == 'no':
        return False
    else:
        print("Invalid input, please choose between yes and no.")
        return repeat()

def algebra():
    while True:
        try:
            choice3 = int(input("Choose between:\n1. Equations\n2. Inequations\n3. Factorize\n4. Functions"))

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


            if choice3 == 1:
                type_of_equation = int(input("What type of equation do you want to solve?\n1. Develop a factorized equation\n2. Resolve an equations"))

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
                    print("Error: Invalid input, please enter either 1 or 2")
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

                function_define = input("Enter the function's range: (e.g., -10, 10 ): ").strip().lower()
                try:
                    range_values = [int(i.strip()) for i in function_define.split(',')]
                    if len(range_values) != 2 or range_values[0] >= range_values[1]:
                        raise ValueError
                except ValueError:
                    print("Invalid range. Please enter a valid range like '-10, 10'.")
                    continue
                function_input = input("Enter the function's formula: (e.g., x^2 +2x +1 ): ").lower().strip()
                function_formula = process_input(function_input)

                expr = sympify(function_formula)

                x_values = range(range_values[0], range_values[1] + 1)
                y_values = [expr.subs(x, val) for val in x_values]

                plt.plot(x_values, y_values, label=f"f(x) = {function_input}", color='red')

                plt.title(f"Graph of f(x) = {format_output(function_formula)}")
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

            else:
                print("Error: Invalid input, please enter 1, 2, 3 or 4")
                continue

        except ValueError:
            print("Invalid input, please enter numbers only.")
            continue
        if not repeat():
            break

algebra()
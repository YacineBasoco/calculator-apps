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

def arithmetic():
    while True:
        try:
            choice1 = int(input("Choose between:\n1. Simple\n2. Operations\n"))

            if choice1 == 1:
                choice = int(input("Which simple equation would you like to solve?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Square root\n"))

                if choice == 6:
                    a = float(input("a = "))
                else:
                    a = float(input("a = "))
                    b = float(input("b = "))

                if choice == 1:
                    add = a + b
                    print(f"The sum of {a} and {b} is {add:.2f}.")
                elif choice == 2:
                    sub = a - b
                    print(f"The difference of {a} and {b} is {sub:.2f}.")
                elif choice == 3:
                    mult = a * b
                    print(f"The product of {a} and {b} is {mult:.2f}.")
                elif choice == 4:
                    div = a / b if b != 0 else "undefined (division by zero)"
                    if b != 0:
                        print(f"The quotient of {a} and {b} is {div:.2f}.")
                    else:
                        print("Error: You can not divide by zero.")
                elif choice == 5:
                    power = a**b
                    print(f"{a} to the power of {b} is {power:.2f}.")
                elif choice == 6:
                    sqrt = math.sqrt(a)
                    print(f"The square root of {a} is {sqrt:.2f}.")
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    continue
            elif choice1 == 2:
                expr = input("Enter an operation to solve: (e.g., (3 + 7)*2/6^2  ): ").strip().lower()

                try:
                    expr = expr.replace('^', '**')
                    result = sympify(expr)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Invalid expression: {e}")

        except (ValueError, TypeError):
            print("Error, Invalid input, please enter an integer.")
            continue
        if not repeat():
            break
def geometry():
    while True:
        try:
            choice2 = int(input("Choose between:\n1. Pythagorean theorem\n2. Circumference\n3. Area\n4. Volume\n5. Perimeter\n"))

            if choice2 == 1:
                base = float(input("Enter base = "))
                height = float(input("Enter height = "))
                pythagorean = math.sqrt(base ** 2 + height ** 2)
                print("The value of the hypotenuse is", round(pythagorean, 2))
            elif choice2 == 2:
                radius = float(input("Enter the radius of the circle: "))
                circumference = 2 * math.pi * radius
                print("The circumference of the circle is", round(circumference, 2))
            elif choice2 == 3:
                dimension = input("Is your shape 2D or 3D? ").strip().lower()
                if dimension == '2d':
                    def calculate_2d_shape():
                        shape = int(input("Which shape's area would you like to calculate?\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n"))

                        if shape == 1:
                            side = float(input("side = "))
                            area = round(side ** 2, 2)
                            print(f"The area of the square is {area} unit².")
                        elif shape == 2:
                            length = float(input("length = "))
                            width = float(input("width = "))
                            area = round(length * width, 2)
                            print(f"The area of the rectangle is {area} unit².")
                        elif shape == 3:
                            base = float(input("base = "))
                            height = float(input("height = "))
                            area = round(0.5 * base * height, 2)
                            print(f"The area of the triangle is {area} unit².")
                        elif shape == 4:
                            radius = float(input("radius = "))
                            area = round(math.pi * radius ** 2, 2)
                            print(f"The area of the circle is {area} unit².")
                        else:
                            print("Error: Invalid input, please choose a valid option.")

                    calculate_2d_shape()
                elif dimension == '3d':
                    def calculate_3d_shape():
                        shape = int(input("Which shape's surface area would you like to calculate?\n1. Cube\n2. Sphere\n3. Cylinder\n4. Cone\n5. Rectangular prism\n6. Pyramid\n7. Torus\n"))

                        if shape == 1:
                            side = float(input("side = "))
                            area = round(6 * side ** 2, 2)
                            print(f"The surface area of the cube is {area} unit².")
                        elif shape == 2:
                            radius = float(input("radius = "))
                            area = round(4 * math.pi * radius ** 2, 2)
                            print(f"The surface area of the sphere is {area} unit².")
                        elif shape == 3:
                            radius = float(input("radius = "))
                            height = float(input("height = "))
                            area = round(2 * math.pi * radius * (height + radius), 2)
                            print(f"The surface area of the cylinder is {area} unit².")
                        elif shape == 4:
                            radius = float(input("radius = "))
                            slant_height = float(input("slant height = "))
                            area = round(math.pi * radius * (slant_height + radius), 2)
                            print(f"The surface area of the cone is {area} unit².")
                        elif shape == 5:
                            length = float(input("length = "))
                            width = float(input("width = "))
                            height = float(input("height = "))
                            area = round(2*(length*width + width*height + length*height), 2)
                            print(f"The surface area of the rectangular prism is {area} unit².")
                        elif shape == 6:
                            base = float(input("base = "))
                            slant_height = float(input("slant height = "))
                            area = round(base**2+0.5*(4*base)*slant_height, 2)
                            print(f"The surface area of the pyramid is {area} unit².")
                        elif shape == 7:
                            R = float(input("major radius (R) = "))
                            r = float(input("radius (r) = "))
                            area = round(4*(math.pi**2)*R*r, 2)
                            print(f"The surface area of the torus is {area} unit².")
                        else:
                            print("Error: Invalid input, please choose a valid option.")
                    calculate_3d_shape()
                else:
                    print("Error: Invalid input, please choose between 2D and 3D.")
            elif choice2 == 4:
                shape = int(input("Which shape's volume would you like to calculate?\n1. Cube\n2. Sphere\n3. Cylinder\n4. Cone\n5. Rectangular prism\n6. Pyramid\n7. Torus\n"))

                if shape == 1:
                    side = float(input("side = "))
                    volume = round(side ** 3, 2)
                    print(f"The volume of the cube is {volume} unit³.")
                elif shape == 2:
                    radius = float(input("radius = "))
                    volume = round(4 / 3 * math.pi * radius ** 3, 2)
                    print(f"The volume of the sphere is {volume} unit³.")
                elif shape == 3:
                    radius = float(input("radius = "))
                    height = float(input("height = "))
                    volume = round(math.pi * radius ** 2 * height, 2)
                    print(f"The volume of the cylinder is {volume} unit³.")
                elif shape == 4:
                    radius = float(input("radius = "))
                    height = float(input("height = "))
                    volume = round(1 / 3 * math.pi * radius ** 2 * height, 2)
                    print(f"The volume of the cone is {volume} unit³.")
                elif shape == 5:
                    length = float(input("length = "))
                    width = float(input("width = "))
                    height = float(input("height = "))
                    volume = round(length*width*height, 2)
                    print(f"The volume of the rectangular prism is {volume} unit³.")
                elif shape == 6:
                    base = float(input("base = "))
                    height = float(input("height = "))
                    volume = round((1/3)*base**2*height, 2)
                    print(f"The volume of the pyramid is {volume} unit³.")
                elif shape == 7:
                    R = float(input("major radius (R) = "))
                    r = float(input("radius (r) = "))
                    volume = round(2*math.pi**2*R*r**2, 2)
                    print(f"The volume of the torus is {volume} unit³.")
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    continue
            elif choice2 == 5:
                shape = int(input("Which shape's perimeter would you like to calculate?\n1. Square\n2. Rectangle\n3. Triangle\n4. Pentagon\n5. Hexagon\n"))

                if shape == 1:
                    side = float(input("side = "))
                    perimeter = round(4 * side, 2)
                    print(f"The perimeter of the square is {perimeter} units.")
                elif shape == 2:
                    length = float(input("length = "))
                    width = float(input("width = "))
                    perimeter = round(2 * (length + width), 2)
                    print(f"The perimeter of the rectangle is {perimeter} units.")
                elif shape == 3:
                    side1 = float(input("side 1 = "))
                    side2 = float(input("side 2 = "))
                    side3 = float(input("side 3 = "))
                    perimeter = round(side1 + side2 + side3, 2)
                    print(f"The perimeter of the triangle is {perimeter} units.")
                elif shape == 4:
                    side = float(input("side = "))
                    perimeter = round(5 * side, 2)
                    print(f"The perimeter of the pentagon is {perimeter} units.")
                elif shape == 5:
                    side = float(input("side = "))
                    perimeter = round(6 * side, 2)
                    print(f"The perimeter of the hexagon is {perimeter} units.")
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    continue
            else:
                print("Error: Invalid input, please choose a valid option.")
                continue

        except (ValueError, TypeError):
            print("Error, Invalid input, please enter an integer.")
            continue
        if not repeat():
            break
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
def statistics():
    currency = input("What currency will you be using?\n")
    while True:
        try:
            choice4 = int(input("What do you want to calculate?\n1. Investments\n2. Average\n"))

            if choice4 == 1:
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
                            print("Error: Invalid input, please enter either 'days', 'months', or 'years'.")

                    total = float(input("How much money do you need in total?\n"))
                    savings = float(input("How much money are you starting with?\n"))
                    finish_line = float(input(f"In how many {word}s do you need {total:.0f}{currency}?\n"))*multiplier

                    if finish_line <= 0:
                        print("Error: The time period must be greater than 0.")
                    else:
                        add = (total - savings) / finish_line
                        print(f"You need to save {add:.2f}{currency} per day to reach your goal.")
            elif choice4 == 2:
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
            choice5 = int(input("Choose between:\n1. Calculus\n2. Finantial Mathematics\n"))
            if choice5 == 1:
                choice = int(input("Choose between:\n1. Differentiation (derivatives)\n2. Intergration (integrals)"))

                if choice == 1:
                    print("idk calculus yet")
                elif choice == 2:
                    print("idk calculus yet")
                else:
                    print("Error: Invalid input, please choose a valid option.")
                    continue
            elif choice5 == 2:
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
                continue

        except (ValueError, TypeError):
            print("Error, Invalid input, please enter an integer.")
            continue
        if not repeat():
            break


while True:
    try:
        section = int(input("Choose between:\n1. Arithmetics\n2. Geometry\n3. Algebra\n4. Statistics\n5. Advanced math\n"))

        if section == 1:
            arithmetic()
            break
        elif section == 2:
            geometry()
            break
        elif section == 3:
            algebra()
            break
        elif section == 4:
            statistics()
            break
        elif section == 5:
            advanced_math()
            break
        else:
            print("Error: Invalid input, please enter either '1', '2', '3' or '4'.")
            continue
    except (ValueError, TypeError):
        print("Error, Invalid input, please enter an integer.")

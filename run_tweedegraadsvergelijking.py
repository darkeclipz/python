# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 27-9-2019
import tweedegraadsvergelijking


def ask_number(question):
    answer = input('{}: '.format(question))
    return float(answer)


print('Quadratic Polynomial Solver')
print('The following program solves a quadratic equation of the '
      + 'form ax^2 + bx + c = 0, and shows the solution(s).\n')

try:
    a = ask_number('Coefficient of a')
    b = ask_number('Coefficient of b')
    c = ask_number('Coefficient c')

    x0, x1 = tweedegraadsvergelijking.solve(a, b, c)

    print(x0, x1)

except ValueError as e:
    print('Input must be a number.')

except Exception as e:
    print(e)

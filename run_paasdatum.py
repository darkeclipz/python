import paasdatum


def ask_number(question):
    answer = input('{}: '.format(question))
    return int(answer)


print('Opdracht 3: Paasdatum bepalen')
print('Voer een datum in waarvoor u de eerstvolgende paasdatum wilt berekenen.')

try:
    y = ask_number('Jaar')
    easter = paasdatum.easter_date(y)
    print('Aankomende pasen valt op {}'.format(easter.strftime("%d-%m-%Y")))

except paasdatum.ArgumentError:
    print('Jaar moet na 1900 vallen.')

except ValueError:
    print('Invoer moet een geheel getal zijn.')

except Exception as e:
    print(e)

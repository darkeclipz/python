# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 3-10-2019
import geld


def ask_number(question):
    answer = input('{}: '.format(question))
    return float(answer) if len(answer) > 0 else None


print('Opdracht2: Geld')
print('Bereken de beginwaarde, interest, duur, of de eindwaarde '
      + 'door drie termen in te vullen. De term die leeg blijft '
      + 'wordt berekend met de andere drie.')


try:
    # Gegevens aan de gebruiker vragen.
    start_capital = ask_number('Beginwaarde')
    interest = ask_number('Interestpercentage')
    period = ask_number('Tijdsduur')
    closing_value = ask_number('Slotwaarde')

    # Start kapitaal berekenen als deze leeg is.
    if start_capital is None:
        result = geld.calculate_start_capital(closing_value, interest, period)
        print('Beginwaarde: {}'.format(result))

    # Interestpercentage berekenen als deze leeg is.
    elif interest is None:
        result = geld.calculate_interest(start_capital, period, closing_value)
        print('Interestpercentage: {}'.format(result))

    # Periode berekenen als deze leeg is.
    elif period is None:
        result = geld.calculate_period(start_capital, interest, closing_value)
        print('Tijdsduur: {}'.format(result))

    # Slotwaarde berekenen als deze leeg is.
    elif closing_value is None:
        result = geld.calculate_closing_value(start_capital, interest, period)
        print('Slotwaarde: {}'.format(result))

    else:
        # Alles is ingevuld dus er valt niet iets te berekenen...
        raise Exception('Niet alle variabelen moeten worden ingevuld. Er moet'
                             + ' één leeg blijven.')


except ValueError:
    print('Invoer moet een getal zijn.')

except geld.ArgumentError as e:
    print('Argument {} is niet ingevuld.'.format(e))

except Exception as e:
    print(e)

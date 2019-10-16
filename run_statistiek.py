import statistiek


def ask_numbers(question):
    answer = input('{}: '.format(question))
    if len(answer) == 0:
        raise Exception('Ongeldige invoer.')
    return list(map(int, answer.split()))


try:
    data = ask_numbers('Voer een lijst met getallen in gescheiden door een spatie, bijv. (1 2 3 4)')
    median, mean, spread, sd = statistiek.descriptive_statistics(data)
    print('-- Beschrijvende statistiek --')
    print('Gemiddelde: {}'.format(mean))
    print('Mediaan: {}'.format(median))
    print('Spreiding: {}'.format(spread))
    print('Standaarddeviatie: {}'.format(sd))

except ValueError:
    print('Ongeldige invoer.')

except Exception as e:
    print(e)

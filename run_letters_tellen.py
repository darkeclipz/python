import letters_tellen


def ask_text(question):
    answer = input('{}: '.format(question))
    return answer


def count_letters_in_text(text):
    counted_letters = letters_tellen.count_characters(text)
    for k, v in counted_letters.items():
        if v > 0:
            print('{} komt {} maal voor.'.format(k, v))


print('Opdracht: Letters tellen')
print('Voer een tekst of bestandsnaam in waarvoor de letters worden geteld.')


try:
    text = ask_text('Voer een tekst/bestandsnaam in')

    if len(text) == 0:
        raise Exception('Voer een geldige tekst/bestandsnaam in.')

    if letters_tellen.has_txt_extension(text):
        print('Tekst lezen uit bestand {}'.format(text))
        text = letters_tellen.read_text_from_file(text)

    count_letters_in_text(text)

except FileNotFoundError:
    print('Bestandsnaam niet gevonden, klopt de locatie wel?')

except Exception as e:
    print(e.Message)

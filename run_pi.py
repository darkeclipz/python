import pi
from math import pi as π


def ask_number(question):
    answer = input('{}: '.format(question))
    return int(answer)


print('Opdracht 4: Pi benaderen')
print('Voor een getal n wordt π op drie verschillende manieren benaderd.')


try:
    n = ask_number('Voer een getal in voor n')

    if(n >= 1000):
        raise Exception('n moet kleiner zijn dan 1000.')

    # Benadering berekenen met Euler's methode.
    pi_euler = pi.approximate_pi_euler(n)
    pi_euler_error = (π - pi_euler)
    pi_euler_error_p = pi_euler_error / π * 100

    # Benadering berekenen met de Gregory-Leibniz methode.
    pi_gregory_leibniz = pi.approximate_pi_gregory_leibniz(n)
    pi_gregory_leibniz_error = (π - pi_gregory_leibniz)
    pi_gregory_leibniz_error_p = pi_gregory_leibniz_error / π * 100

    # Benadering berekenen met de Brent-Salamin methode.
    pi_brent_salamin = pi.approximate_pi_brent_salamin(n)
    pi_brent_salamin_error = (π - pi_brent_salamin)
    pi_brent_salamin_error_p = pi_brent_salamin_error / π * 100

    # Uitvoer weergeven.
    print('π (exact) = {}'.format(π))
    print('π (euler) = {0} (error = {1:.4f}, error percentage = {2:.3f}%)'
          .format(pi_euler, pi_euler_error, pi_euler_error_p))
    print('π (gregory-leibniz) = {0} (error = {1:.4f}, error percentage = {2:.3f}%)'
          .format(pi_gregory_leibniz, pi_gregory_leibniz_error, pi_gregory_leibniz_error_p))
    print('π (brent-salamin) = {0} (error = {1:.4f}, error_percentage = {2:.3f}%)'
          .format(pi_brent_salamin, pi_brent_salamin_error, pi_brent_salamin_error_p))

except ValueError:
    print('Invoer moet een geheel getal zijn.')

except Exception as e:
    print(e)

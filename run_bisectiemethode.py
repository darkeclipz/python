import bisectiemethode


# states voor de state machine
STATE_INIT = 0
STATE_SELECT_FUNCTION = 1
STATE_SELECT_INTERVAL = 2
STATE_SOLVE = 3
STATE_SOLUTION = 4
STATE_EXIT = 5
STATE_SELECT_EPSILON = 6


class StateConsole:
    """
    Console applicatie die met een state machine de status opslaat en zo door
    de juiste dialogen gaat.
    """
    state = None  # state van huidige dialog
    f = None  # geselecteerde functie
    interval = (None, None)  # geselecteerde interval
    solution = None  # gevonden oplossing
    epsilon = 0.001  # geselecteerde precisie

    def __init__(self):
        # Dictionary met een functie die d.m.v. de juiste
        # state code wordt aangeroepen.
        self.selector = {
            0: self.init,
            1: self.select_function,
            2: self.select_interval,
            3: self.solve,
            4: self.solution,
            5: quit,
            6: self.select_epsilon
        }
        self.run()

    def ask_number(self, question):
        """
        Getal (float) aan de gebruiker vragen.
        :param question:
        :return:
        """
        answer = input('{}: '.format(question))
        return float(answer)

    def ask_integer(self, question):
        """
        Getal (integer) aan de gebruiker vragen.
        :param question:
        :return:
        """
        answer = input('{}: '.format(question))
        return int(answer)

    def run(self):
        """
        Console applicatie uitvoeren door steeds de juiste methode voor
        de huidige staat aan te roepen.
        :return:
        """
        try:
            self.state = STATE_INIT
            while True:
                self.state = self.selector[self.state]()
        except Exception as e:
            print(e)

    def init(self):
        """
        Initialiseren van console applicatie door een welkomstekst te printen.
        :return:
        """
        print('Opdracht: Bisectiemethode')
        print('Selecteer een functie en een interval waarvoor de oplossing '
              + 'wordt bepaald.')
        return STATE_SELECT_FUNCTION

    def select_function(self):
        """
        State waarin de gebruiker een functie moet selecteren d.m.v. het invoeren
        van een id zoals 0, 1, 2, ...
        :return:
        """
        try:
            for i, f in enumerate(bisectiemethode.functions):
                print('{}: {}'.format(i, f))
            id = self.ask_integer('Selecteer een functie id')
            if not 0 <= id < len(bisectiemethode.functions):
                raise ValueError()
            self.f = bisectiemethode.functions[id]
            return STATE_SELECT_INTERVAL
        except ValueError:
            print('Voer een geldig getal in.')
        return STATE_SELECT_FUNCTION

    def select_interval(self):
        """
        State waarin de gebruik een interval (a, b) moet opgeven.
        :return:
        """
        try:
            a = self.ask_number('Voer het linker interval a in')
            b = self.ask_number('Voer het rechter interval b in')
            if a >= b:
                raise Exception("a moet kleiner dan b zijn.")
            self.interval = (a, b)
            return STATE_SELECT_EPSILON
        except Exception as e:
            print(e)
        return STATE_SELECT_INTERVAL

    def select_epsilon(self):
        """
        State waarin de gebruiker een precisie (epsilon) moet opgeven.
        :return:
        """
        try:
            eps = self.ask_number('Voer een foutmarge (epsilon) in')
            self.epsilon = eps
            return STATE_SOLVE
        except Exception as e:
            print(e)
        return STATE_SELECT_EPSILON

    def solve(self):
        """
        State waarin de oplossing voor de gekozen variabelen wordt gevonden.
        :return:
        """
        try:
            print('Oplossing bepalen voor f(x) = {} met ({}, {}) en epsilon = {}'
                  .format(self.f, *self.interval, self.epsilon))
            self.solution = bisectiemethode.bisection_solver(self.f.f, *self.interval, self.epsilon)
            return STATE_SOLUTION
        except Exception as e:
            print(e)
        return STATE_SELECT_FUNCTION

    def solution(self):
        """
        State waarin de oplossing wordt weergegeven, en daarna afsluit.
        :return:
        """
        print('De oplossing is x = {}'.format(self.solution))
        return STATE_EXIT


if __name__ == '__main__':
    StateConsole()

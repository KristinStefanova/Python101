class Parser:
    def __init__(self, polinom):
        if type(polinom) is not str:
            raise TypeError
        self.polinomial_list = polinom.split('+')

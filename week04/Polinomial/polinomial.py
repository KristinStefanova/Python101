from parse_string_to_polinomial import Parser


class Polinomial:
    def __init__(self, function):
        self._function = function
        self._parser = Parser(function)

    def __str__(self):
        return f'f(x) = {self._function}'

    def __repr__(self):
        return f'f(x) = {self._function}'

    def __eq__(self, other):
        return self._function == other._function


class FirstDerivative(Polinomial):
    def __init__(self, function):
        super().__init__(function)
        self._derivative = self.make_derivative()

    def __str__(self):
        return f"f'(x) = {self._derivative}"

    def __repr__(self):
        return f"f'(x) = {self._derivative}"

    def __eq__(self, other):
        return self._derivative == other._derivative

    def make_derivative_list(self):
        derivative_list = []
        for item in self._parser.polinomial_list:
            if '*' in item and '^' in item:
                indx_of_multi = item.find('*')
                indx_of_power = item.find('^')
                power = int(item[indx_of_power + 1:]) - 1
                coeff = int(item[:indx_of_multi]) * (power + 1)
                derivative_list.append(f'{coeff}*x^{power}')
            elif '*' in item and '^' not in item:
                indx_of_multi = item.find('*')
                coeff = int(item[:indx_of_multi])
                derivative_list.append(str(coeff))
            elif '^' in item and '*' not in item:
                indx_of_power = item.find('^')
                power = int(item[indx_of_power + 1:])
                coeff = power
                derivative_list.append(f'{coeff}*x^{power - 1}')
            elif item.isdigit():
                derivative_list.append("0")
            else:
                derivative_list.append("1")
        return derivative_list

    def make_derivative(self):
        derivative_list = self.make_derivative_list()
        new_derivative_list = []
        for item in derivative_list:
            if 'x^1' in item:
                new_derivative_list.append(item.replace('x^1', 'x'))
            elif '0' == item and len(derivative_list) > 1:
                continue
            elif 'x^0' in item:
                new_derivative_list.append(item.replace('x^0', '1'))
            elif '1*x' in item:
                new_derivative_list.append(item.replace('1*x', 'x'))
            else:
                new_derivative_list.append(item)
        return '+'.join(new_derivative_list)

    def get_derivative(self):
        return self._derivative

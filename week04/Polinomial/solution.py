import sys
from polinomial import Polinomial, FirstDerivative


def main():
    try:
        polinom = sys.argv[1]
    except IndexError:
        print("You did not provide a polinomial!")
    else:
        polinomial = Polinomial(polinom)
        derivative = FirstDerivative(polinom)
        print(f"The derivative of {polinomial} is: ")
        print(derivative)


if __name__ == '__main__':
    main()

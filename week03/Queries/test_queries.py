import unittest
from queries import filter_by_one_agrument
from queries import filter_by_one_argument_that_startswith
from queries import filter_by_one_argument_that_contains
from queries import filter_by_one_argument_greater_than
from queries import filter_by_one_argument_less_than
from queries import filter_by_with_order_by
from queries import filter, count, first, last


class FilterTests(unittest.TestCase):
    def test_filter_by_one_agrument_with_my_file(self):
        my_file = [['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                   ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                   ['Marilyn Maldonado', 'black', 'Walker PLC',
                    'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                   ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                    'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                   ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                    'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                    '3779'],
                   ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039'],
                   ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']]
        expected = [['Michael Olson', 'olive', 'Scott, Young and King',
                     'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151']]
        self.assertEqual(
            filter_by_one_agrument(my_file, 0, "Michael Olson"), expected)

    def test_filter_by_one_argument_that_startswith(self):
        my_file = [['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                   ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                   ['Marilyn Maldonado', 'black', 'Walker PLC',
                    'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                   ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                    'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                   ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                    'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                    '3779'],
                   ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039'],
                   ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']]
        expected = [['Marilyn Maldonado', 'black', 'Walker PLC',
                     'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                    ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                     'eileen88@hotmail.com', '659-155-8389x092', '8587']]
        self.assertEqual(
            filter_by_one_argument_that_startswith(my_file, 0, "Mar"),
            expected)

    def test_filter_by_one_argument_that_contains(self):
        my_file = [['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                   ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                   ['Marilyn Maldonado', 'black', 'Walker PLC',
                    'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                   ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                    'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                   ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                    'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                    '3779'],
                   ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039'],
                   ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']]
        expected = [['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                     'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                    ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                     'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                     '3779'],
                    ['Patricia King', 'white', 'Gonzalez-Fuentes',
                     'kimberlyrasmussen@hotmail.com', '1-512-204-5161',
                     '1039'],
                    ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                     'crystal69@hotmail.com', '(664)760-9409', '1995']]
        self.assertEqual(
            filter_by_one_argument_that_contains(my_file, 3, "@hotmail"),
            expected)

    def test_filter_by_one_argument_greater_than(self):
        my_file = [['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                   ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                   ['Marilyn Maldonado', 'black', 'Walker PLC',
                    'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                   ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                    'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                   ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                    'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                    '3779'],
                   ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039'],
                   ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']]
        expected = [['Diana Harris', 'lime', 'Martin-Barnes',
                     'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                    ['Marilyn Maldonado', 'black', 'Walker PLC',
                     'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                    ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                     'eileen88@hotmail.com', '659-155-8389x092', '8587']]
        self.assertEqual(
            filter_by_one_argument_greater_than(my_file, 5, 5000),
            expected)

    def test_filter_by_one_argument_less_than(self):
        my_file = [['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                   ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                   ['Marilyn Maldonado', 'black', 'Walker PLC',
                    'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                   ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                    'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                   ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                    'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                    '3779'],
                   ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039'],
                   ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']]
        expected = [['Michael Olson', 'olive', 'Scott, Young and King',
                     'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                    ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                     'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                     '3779'],
                    ['Patricia King', 'white', 'Gonzalez-Fuentes',
                     'kimberlyrasmussen@hotmail.com', '1-512-204-5161',
                     '1039'],
                    ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                     'crystal69@hotmail.com', '(664)760-9409', '1995']]
        self.assertEqual(
            filter_by_one_argument_less_than(my_file, 5, 5000),
            expected)

    def test_filter_by_with_order_by_salary(self):
        my_file = [['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                   ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                   ['Marilyn Maldonado', 'black', 'Walker PLC',
                    'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                   ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                    'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                   ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                    'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                    '3779'],
                   ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039'],
                   ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']]
        expected = [['Patricia King', 'white', 'Gonzalez-Fuentes',
                     'kimberlyrasmussen@hotmail.com', '1-512-204-5161',
                     '1039'],
                    ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                     'crystal69@hotmail.com', '(664)760-9409', '1995'],
                    ['Michael Olson', 'olive', 'Scott, Young and King',
                     'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                    ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                     'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                     '3779'],
                    ['Diana Harris', 'lime', 'Martin-Barnes',
                     'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                    ['Marilyn Maldonado', 'black', 'Walker PLC',
                     'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                    ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                     'eileen88@hotmail.com', '659-155-8389x092', '8587']]
        self.assertEqual(filter_by_with_order_by(my_file, 5), expected)

    def test_filter_by_with_order_by_name(self):
        my_file = [['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                   ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                   ['Marilyn Maldonado', 'black', 'Walker PLC',
                    'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                   ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                    'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                   ['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                    'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                    '3779'],
                   ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039'],
                   ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']]
        expected = [['Amanda Hughes', 'maroon', 'Franco, Harvey and Payne',
                     'wilkinsonjason@hotmail.com', '1-366-403-5794x0781',
                     '3779'],
                    ['Diana Harris', 'lime', 'Martin-Barnes',
                     'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                    ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                     'crystal69@hotmail.com', '(664)760-9409', '1995'],
                    ['Marilyn Maldonado', 'black', 'Walker PLC',
                     'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
                    ['Marissa Carter', 'olive', 'Hart, Ray and Wagner',
                     'eileen88@hotmail.com', '659-155-8389x092', '8587'],
                    ['Michael Olson', 'olive', 'Scott, Young and King',
                     'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                    ['Patricia King', 'white', 'Gonzalez-Fuentes',
                     'kimberlyrasmussen@hotmail.com', '1-512-204-5161',
                     '1039']]
        self.assertEqual(filter_by_with_order_by(my_file, 0), expected)

    def test_filter_with_empty_file(self):
        my_file = "empty_file.csv"
        expected = []
        self.assertEqual(filter(my_file, full_name="Diana Harris",
                                favourite_color="lime"), expected)

    def test_filter_with_empty_file_whether_raise_exception(self):
        my_file = "empty_file.csv"
        with self.assertRaises(Exception) as e:
            self.assertTrue(filter(my_file, full_name="Diana Harris",
                                   favourite_color="lime"), e.exception)

    def test_filter_by_first_name_and_favourite_color(self):
        my_file = "test_data.csv"
        expected = [['Diana Harris', 'lime', 'Martin-Barnes',
                     'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter(my_file, full_name="Diana Harris",
                                favourite_color="lime"), expected)

    def test_filter_by_first_name_that_startswith(self):
        my_file = "test_data.csv"
        expected = [['Diana Harris', 'lime', 'Martin-Barnes',
                     'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter(my_file, full_name__startswith="Diana Harris"),
                         expected)

    def test_filter_by_email_that_contains(self):
        my_file = "test_data.csv"
        expected = [['Diana Harris', 'lime', 'Martin-Barnes',
                     'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter(my_file, email__contains="@gmail"), expected)

    def test_filter_by_salary_gt_1000_and_lt_3000(self):
        my_file = "test_data.csv"
        expected = [['Michael Olson', 'olive', 'Scott, Young and King',
                     'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151'],
                    ['Patricia King', 'white', 'Gonzalez-Fuentes',
                     'kimberlyrasmussen@hotmail.com', '1-512-204-5161',
                     '1039'],
                    ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                     'crystal69@hotmail.com', '(664)760-9409', '1995']]
        self.assertListEqual(filter(my_file, salary__gt=1000, salary__lt=3000),
                             expected)

    def test_filter_by_salary_gt_1000_and_lt_3000_order_by_salary(self):
        my_file = "test_data.csv"
        expected = [['Patricia King', 'white', 'Gonzalez-Fuentes',
                     'kimberlyrasmussen@hotmail.com', '1-512-204-5161',
                     '1039'],
                    ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                     'crystal69@hotmail.com', '(664)760-9409', '1995'],
                    ['Michael Olson', 'olive', 'Scott, Young and King',
                     'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151']]
        self.assertListEqual(filter(my_file, salary__gt=1000, salary__lt=3000,
                                    order_by='salary'), expected)

    def test_count_by_first_name_and_favourite_color(self):
        my_file = "test_data.csv"
        expected = 1
        self.assertEqual(count(my_file, full_name="Diana Harris",
                               favourite_color="lime"), expected)

    def test_count_by_first_name_that_startswith(self):
        my_file = "test_data.csv"
        expected = 1
        self.assertEqual(count(my_file, full_name__startswith="Diana Harris"),
                         expected)

    def test_count_by_email_that_contains(self):
        my_file = "test_data.csv"
        expected = 1
        self.assertEqual(count(my_file, email__contains="@gmail"), expected)

    def test_count_by_salary_gt_1000_and_lt_3000(self):
        my_file = "test_data.csv"
        expected = 3
        self.assertEqual(count(my_file, salary__gt=1000, salary__lt=3000),
                         expected)

    def test_count_by_salary_gt_1000_and_lt_3000_order_by_salary(self):
        my_file = "test_data.csv"
        expected = 3
        self.assertEqual(count(my_file, salary__gt=1000, salary__lt=3000,
                               order_by='salary'), expected)

    def test_first_by_first_name_and_favourite_color(self):
        my_file = "test_data.csv"
        expected = ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354']
        self.assertEqual(first(my_file, full_name="Diana Harris",
                               favourite_color="lime"), expected)

    def test_first_by_first_name_that_startswith(self):
        my_file = "test_data.csv"
        expected = ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354']
        self.assertEqual(first(my_file, full_name__startswith="Diana Harris"),
                         expected)

    def test_first_by_email_that_contains(self):
        my_file = "test_data.csv"
        expected = ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354']
        self.assertEqual(first(my_file, email__contains="@gmail"), expected)

    def test_first_by_salary_gt_1000_and_lt_3000(self):
        my_file = "test_data.csv"
        expected = ['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151']
        self.assertListEqual(first(my_file, salary__gt=1000, salary__lt=3000),
                             expected)

    def test_first_by_salary_gt_1000_and_lt_3000_order_by_salary(self):
        my_file = "test_data.csv"
        expected = ['Patricia King', 'white', 'Gonzalez-Fuentes',
                    'kimberlyrasmussen@hotmail.com', '1-512-204-5161', '1039']
        self.assertListEqual(first(my_file, salary__gt=1000, salary__lt=3000,
                                   order_by='salary'), expected)

    def test_last_by_first_name_and_favourite_color(self):
        my_file = "test_data.csv"
        expected = ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354']
        self.assertEqual(last(my_file, full_name="Diana Harris",
                              favourite_color="lime"), expected)

    def test_last_by_first_name_that_startswith(self):
        my_file = "test_data.csv"
        expected = ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354']
        self.assertEqual(last(my_file, full_name__startswith="Diana Harris"),
                         expected)

    def test_last_by_email_that_contains(self):
        my_file = "test_data.csv"
        expected = ['Diana Harris', 'lime', 'Martin-Barnes',
                    'timothy81@gmail.com', '1-860-251-9980x6941', '5354']
        self.assertEqual(last(my_file, email__contains="@gmail"), expected)

    def test_last_by_salary_gt_1000_and_lt_3000(self):
        my_file = "test_data.csv"
        expected = ['Julie Byrd', 'lime', 'Johnson-Reynolds',
                    'crystal69@hotmail.com', '(664)760-9409', '1995']
        self.assertListEqual(last(my_file, salary__gt=1000, salary__lt=3000),
                             expected)

    def test_last_by_salary_gt_1000_and_lt_3000_order_by_salary(self):
        my_file = "test_data.csv"
        expected = ['Michael Olson', 'olive', 'Scott, Young and King',
                    'zacharymcdonald@yahoo.com', '114-116-1124x315', '2151']
        self.assertListEqual(last(my_file, salary__gt=1000, salary__lt=3000,
                                  order_by='salary'), expected)


if __name__ == '__main__':
    unittest.main()

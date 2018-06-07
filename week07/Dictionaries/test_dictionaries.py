import unittest
from dictionaries import deep_find, schema_validator


class DictionariesTests(unittest.TestCase):
    def setUp(self):
        self.first = {"a": 1,
                      "b": 2,
                      "c": 3,
                      "d": 4,
                      "e": 5,
                      "f": 6}
        self.second = {"a": 1,
                       "b": {"g": 7, "h": 8},
                       "c": [{"j": 9, "k": 10}, {"l": 11, "m": 12}],
                       "d": 4,
                       "e": ({"n": 13, "o": 14}, {"q": 13, "z": 14}),
                       "f": 6}

    def test_deep_find_with_first_dict(self):
        with self.subTest("test with correct key"):
            expected = 3
            actual = deep_find(self.first, 'c')
            self.assertEqual(expected, actual)

        with self.subTest("test with wrong key"):
            expected = None
            actual = deep_find(self.first, 't')
            self.assertEqual(expected, actual)

    def test_deep_find_with_second_dict(self):
        with self.subTest("test with correct key"):
            expected = 8
            actual = deep_find(self.second, 'h')
            self.assertEqual(expected, actual)

        with self.subTest("test with correct key"):
            expected = 10
            actual = deep_find(self.second, 'k')
            self.assertEqual(expected, actual)

        with self.subTest("test with correct key"):
            expected = 13
            actual = deep_find(self.second, 'n')
            self.assertEqual(expected, actual)

    def test_schema_validator(self):
        with self.subTest("Valid data and schema"):
            schema = [
                'key1',
                'key2',
                [
                    'key3',
                    ['inner_key1', 'inner_key2']
                ]
            ]
            data = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': {
                    'inner_key1': 'val1',
                    'inner_key2': 'val2'
                }
            }
            self.assertTrue(schema_validator(schema, data))

        with self.subTest("Invalid data and schema"):
            schema = [
                'key1',
                'key2',
                [
                    'key3',
                    ['inner_key1', 'inner_key2']
                ]
            ]
            data = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': {
                    'inner_key1': 'val1',
                    'inner_key2': 'val2'
                },
                'key4': 'not expected'
            }
            self.assertFalse(schema_validator(schema, data))

        with self.subTest("one level Invalid data and schema"):
            schema = [
                'key1',
                ['inner_key1', 'inner_key2']
            ]
            data = {
                'key1': {
                    'inner_key1': 'val1',
                    'inner_key2': 'val2'
                }
            }
            self.assertTrue(schema_validator(schema, data))

        with self.subTest("one level Invalid data and schema"):
            schema = [
                'key1',
                ['inner_key1']
            ]
            data = {
                'key1': {
                    'inner_key1': 'val1',
                    'inner_key2': 'val2'
                }
            }
            self.assertFalse(schema_validator(schema, data))

        with self.subTest("FALSE Plain data with less keys"):
            schema = ['key1', 'key2']
            data = {'key1': 'val1'}
            self.assertFalse(schema_validator(schema, data))

        with self.subTest("TRUE Plain data with less keys"):
            schema = ['key1', 'key2']
            data = {'key1': 'val1', 'key2': 'val2'}
            self.assertTrue(schema_validator(schema, data))

        with self.subTest("Valid data and schema"):
            schema = [
                'key1',
                'key2',
                [
                    'key3',
                    ['inner_key1', ['inner_inner_key1', 'inner_inner_key2']]
                ]
            ]
            data = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': {
                    'inner_key1': {
                        'inner_inner_key1': 'in_val1',
                        'inner_inner_key2': 'in_val2',
                    }
                }
            }
            self.assertTrue(schema_validator(schema, data))

        with self.subTest("Invalid data and schema"):
            schema = [
                'key1',
                'key2',
                [
                    'key3',
                    ['inner_key1', ['inner_inner_key2']]
                ]
            ]
            data = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': {
                    'inner_key1': {
                        'inner_inner_key1': 'in_val1',
                        'inner_inner_key2': 'in_val2',
                    }
                }
            }
            self.assertFalse(schema_validator(schema, data))


if __name__ == '__main__':
    unittest.main()

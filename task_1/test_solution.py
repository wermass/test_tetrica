import unittest
from solution import strict, sum_two


class TestStrictDecorator(unittest.TestCase):

    def test_valid_arguments(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_invalid_argument_type(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.5)

    def test_no_annotations(self):
        @strict
        def no_annotations(a, b):
            return a + b

        self.assertEqual(no_annotations(1, 2), 3)

    def test_mixed_argument_types(self):
        @strict
        def concat_strings(a: str, b: str) -> str:
            return a + b

        self.assertEqual(concat_strings("Hello, ", "World!"), "Hello, World!")
        with self.assertRaises(TypeError):
            concat_strings("Hello, ", 5)


if __name__ == "__main__":
    unittest.main()

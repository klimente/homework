

def sqrt(value):
    """ Calculate

    :param value: source value
    :type value: int
    :returns: float -- result of calculate
    """
    if value <= 0:
        raise ValueError('Positive value required')
    return value ** 0.5

import unittest

class Testsqrt(unittest.TestCase):
    def test_squeres_root(self):
        self.assertEqual(sqrt(9),3.0)
    def test_non_squeres_root(self):
        with self.assertRaises(ValueError) as raised:
            sqrt(1)
        self.assertEqual(raised.args[0])

if __name__ == '__main__':
    unittest.main()
#unit test testi
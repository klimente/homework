import unittest
import stats
from unittest.mock import patch

class TestStats(unittest.TestCase):


    def test_data_validator_decorator_works(self):
        with self.assertRaises(TypeError) as raised_exception:
            stats.get_numeric_column(2, 3, 4)
        self.assertEqual(raised_exception.exception.args[0], "Data must be list type")
        with self.assertRaises(ValueError) as raised_exception:
            stats.get_numeric_column([2,3,4])
        self.assertEqual(raised_exception.exception.args[0], "value in data must be list")
        with self.assertRaises(TypeError) as raised_exception:
            stats.get_numeric_column([[2,3,4]], 3.5)
        self.assertEqual(raised_exception.exception.args[0], "Col num must be int")


    def test_get_numeric_column(self):
        self.assertEqual(stats.get_numeric_column([
            [1, 2, 3],
            [1, 2, 3]
        ], 2),
            [3, 3]
        )
        self.assertEqual(stats.get_numeric_column([
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 'NA']
        ],
            2, missing_data=True),
            [3, 3, 3]
        )
        self.assertEqual(stats.get_numeric_column([
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 'NA']
        ], 2),
            [3, 3]
        )


    def test_convert_str_to_numeric(self):
        self.assertEqual(stats.convert_str_to_numeric([
            ['1 3', '2 000', '4 020'],
            ['1 3', '2 000', '4 020'],
            ['3 4', '2 3', 'NA']
        ], 2),
            [4020.0, 4020.0])
        self.assertEqual(
            stats.convert_str_to_numeric([
                ['1 3', '2 000', '4 020'],
                ['1 3', '2 000', '4 020'],
                ['3 4', '2 3', 'NA']
            ], 2, missing_data=True),
            [4020.0, 4020.0, 4020.0]
        )


    def test_validator_working_correct_negativa(self):
        with self.assertRaises(TypeError) as raised_exception:
            stats.missing_data(2, 3.5)
        self.assertEqual(raised_exception.exception.args[0], "input type must be list")
        with self.assertRaises(ValueError) as raised_exception:
            stats.mean([1, 2, (2, 3.5)], [3.5, 2, 1])
        self.assertEqual(raised_exception.exception.args[0], "value in x must be numeric")


    def test_missing_data(self):
        self.assertEqual(
            stats.missing_data([1, 2, 2], [3.5, 2, 1]),
            0.0
        )


    def test_missing_data_exception_wrong_data_negative(self):
        with self.assertRaises(TypeError) as raised_exception:
            stats.missing_data([2], 3.5)
        self.assertEqual(raised_exception.exception.args[0], 'data type must be list')


    def test_mean(self):
        self.assertEqual(
            stats.mean([2, 2, 2, 2]),
            2
        )
        self.assertAlmostEqual(
            stats.mean([1, 2, 3, 4]),
            2.5
        )


    def test_median(self):
        self.assertEqual(
            stats.median([1, 2, 3, 4]),
            2.5
        )
        self.assertEqual(
            stats.median([1, 2, 3, 4, 5]),
            3
        )


    def test_mode(self):
        self.assertEqual(
            stats.mode([1, 2, 3, 4, 2]),
            [2]
        )
        self.assertEqual(
            stats.mode([1, 2]),
            [1, 2]
        )


    def test_quantile(self):
        self.assertEqual(
            stats.quantile([1, 2, 3, 4, 5], 0.2),
            2
        )


    def test_data_ranhe(self):
        self.assertEqual(
            stats.data_range([1, 2, 3, 4, 5]),
            4
        )


    def test_plot_function_work(self):
        self.assertEqual(
            stats.box_plot([[1, 2, 3], [1, 4, 5]]),
            None
        )


    def test_variance(self):
        self.assertEqual(
            stats.variance([1, 2, 3, 4, 5]),
            2.5
        )


    def test_std(self):
        self.assertAlmostEqual(
            stats.std([1, 2, 3, 4, 5]),
            1.5811,
            places=4
        )


    def test_covarience(self):
        self.assertEqual(
            stats.covarience([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            2.5
        )


    def test_covarience_wrong_type_y(self):
        with self.assertRaises(TypeError) as raised_exception:
            stats.covarience([2, 3, 4], 's')
        self.assertEqual(raised_exception.exception.args[0], "y type must be list")


    def test_covarience_wrong_value_y(self):
        with self.assertRaises(ValueError) as raised_exception:
            stats.covarience([2, 3, 4], [1, 2, 3, 's'])
        self.assertEqual(raised_exception.exception.args[0], "value in x must be numeric")


    def test_covarience_different_sizes(self):
        with self.assertRaises(ValueError) as raised_exception:
            stats.covarience([2, 3, 4], [1, 2, 3, 5])
        self.assertEqual(raised_exception.exception.args[0], "x and y must have the same size")


    def test_correlation(self):
        self.assertAlmostEqual(stats.correlation(
            [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            1,
            delta=0.00001)


    def test_correlation_with_zero_std(self):
        self.assertEqual(
            stats.correlation([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),
            0)


    def test_pdf_works(self):
        self.assertEqual(
            stats.pdf([1, 2, 3, 4, 5]),
            {1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.2}
        )


    def test_cdf_works(self):
        self.assertEqual(
            stats.cdf([1, 2, 3, 4, 5]),
            {1: 0.2, 2: 0.4, 3: 0.6, 4: 0.8, 5: 1.0}
        )

    def test_quantile_wrong_range_p(self):
        with self.assertRaises(ValueError) as raised_exception:
            stats.quantile([2, 3, 4], 3.0)
        self.assertEqual(raised_exception.exception.args[0], "p must be in range (0,1)")

    def test_quantile_wrong_type(self):
        with self.assertRaises(TypeError) as raised_exception:
            stats.quantile([2, 3, 4], 3)
        self.assertEqual(raised_exception.exception.args[0], "p must be float")




if __name__ == '__main__':
    unittest.main()
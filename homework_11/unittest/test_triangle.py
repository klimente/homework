"""
Unittests for triangle module
"""
import io
import unittest
import triangle
import sys
import builtins
import unittest.mock



class TestTriangle(unittest.TestCase):
    def setUp(self):
        """
        Initial state before each test.
        """
        self.tr1 = triangle.Triangle((7, 1), (1, 9), (1, 1))
        self.tr2 = triangle.Triangle((3.0, 0.0), (0.0, 4.0), (0.0, 0.0))
        self.floattest = triangle.Triangle((3.3, 0.0), (0.2, 4.2), (0.0, 0.0))


    def test_all_attributes_of_instance(self):
        """
        Test to check that all attributes has initialized.
        """
        self.assertEqual(self.tr1.point_a, (7.0, 1.0))
        self.assertEqual(self.tr1.point_b, (1.0, 9.0))
        self.assertEqual(self.tr1.point_c, (1.0, 1.0))
        self.assertEqual(self.tr1.len_ab, 10.0)
        self.assertEqual(self.tr1.len_ac, 6.0)
        self.assertEqual(self.tr1.len_bc, 8.0)
        self.assertEqual(self.tr2.point_a, (3.0, 0.0))
        self.assertEqual(self.tr2.point_b, (0.0, 4.0))
        self.assertEqual(self.tr2.point_c, (0.0, 0.0))
        self.assertEqual(self.tr2.len_ab, 5.0)
        self.assertEqual(self.tr2.len_ac, 3.0)
        self.assertEqual(self.tr2.len_bc, 4.0)


    def test_instance_of_triangle_with_coordinates_with_values_ne_2_negative(self):
        """
        Negative test to check exception by putting point with length not equal 2.
        """
        with self.assertRaises(TypeError) as raised_exception:
            triangle.Triangle((1, 2, 3), (2, (3,)), ('c', 5))
        self.assertEqual(raised_exception.exception.args[0],'Coordinates must have only 2 values')


    def test_instace_of_triangle_with_coordinates_that_not_tuples_negative(self):
        """
        Negative test to check exception by putting not correct type in __init__.
        """
        with self.assertRaises(TypeError) as raised_exception:
            triangle.Triangle((1, 2), [2, 3], [3, 4])
        self.assertEqual(raised_exception.exception.args[0], 'Coordinates must be in tuple')

    def test_instance_of_triangle_with_values_of_coordinates_that_not_number_negative(self):
        """
        Negative test to check exception by putting not numeric values in coordinates.
        """
        with self.assertRaises(ValueError) as raised_exception:
            triangle.Triangle((1,2),(2,(3,)), ('c',5))
        self.assertEqual(raised_exception.exception.args[0], 'Coordinate value must be number')

    def test_instance_of_triangle_with_coordinates_that_do_not_form_triangle_negative(self):
        """
        Negative test to check exception by putting incorrect coordinetes to form a triangle.
        And check correct output.
        """
        with self.assertRaises(SystemExit) as raised_exception:
            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            triangle.Triangle((3.0, 0.0), (4.0, 0.0), (5.0, 0.0))
            sys.stdout = sys.__stdout__
        self.assertEqual(capturedOut.getvalue(),
                         'Points ((3.0, 0.0), (4.0, 0.0), (5.0, 0.0)) do not form a triangle\n')
        self.assertEqual(raised_exception.exception.args[0],1)

    def test_privat_method_of_triangle_length_calculate_with_2_or_more_same_points_negative(self):
        """
        Negative test to check exception by putting incorrect coordinates to form triangle.
        And check correct output.
        """
        with self.assertRaises(SystemExit) as raised_exception:
            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            triangle.Triangle((3.0, 0.0), (0.0, 0.0), (0.0, 0.0))
            sys.stdout = sys.__stdout__
        self.assertEqual(capturedOut.getvalue(),
                         'Cannot form triangle. Because coordinates ((0.0, 0.0), (0.0, 0.0)) are the same\n')
        self.assertEqual(raised_exception.exception.args[0], 1)


    def test_get_attribute_of_class_apex_of_triangle(self):
        """
        Test to check attribute of class Triangle.
        """
        self.assertEqual(triangle.Triangle.apex_of_triangle, ('A', 'B', 'C'))

    def test_property_points(self):
        """
        Test to check property points of Triangle calculated right.
        """
        self.assertEqual(self.tr1.points,((7, 1), (1, 9), (1, 1)))
        self.assertEqual(self.tr2.points,((3.0, 0.0), (0.0, 4.0), (0.0, 0.0)))
        self.assertEqual(self.floattest.points, ((3.3, 0.0), (0.2, 4.2), (0.0, 0.0)))

    def test_property_sides(self):
        """
        Test to check property  sides of Triangle calculated right.
        """
        self.assertEqual(self.tr1.sides, (10.0, 6.0, 8.0))
        self.assertEqual(self.tr2.sides, (5.0, 3.0, 4.0))


    def test_property_semiperimetr(self):
        """
        Test to check property semiperimetr calculated right.
        """
        self.assertEqual(self.tr1.semiperimeter,12.0)
        self.assertEqual(self.tr2.semiperimeter,6.0)
        self.assertAlmostEqual(self.floattest.semiperimeter, 6.362456,places=6)


    def test_private_method_length_calculate(self):
        """
        Test to check private method '_length_calculate' of Triangle works fine.
        """
        self.assertEqual(self.tr1._length_calculate((self.tr1.point_a,self.tr1.point_c)),6.0)
        self.assertEqual(self.tr2._length_calculate((self.tr2.point_a,self.tr2.point_c)),3.0)


    def test_private_method__multipliers(self):
        """
        Test to check private method '_multipliers' of Triangle works fine.
        """
        self.assertEqual(self.tr1._multipliers(), (12.0, 2.0, 6.0, 4.0))
        self.assertEqual(self.tr2._multipliers(), (6.0, 1.0, 3.0, 2.0))

    def test_method_area_by_heron(self):
        """
        Test to check method 'area_by_heron' of Triangle works fine.
        """
        self.assertEqual(self.tr1.area_by_heron(), 24.0)
        self.assertEqual(self.tr2.area_by_heron(), 6.0)
        self.assertAlmostEqual(self.floattest.area_by_heron(), 6.929, delta=0.001)

    def test_function_tuple_points(self):
        """
        Test to check function 'tuple_points' makes tuple of values.
        """
        self.assertEqual(triangle.tuple_points(lambda x: x*4, [1, 2, 3, 4]), (4, 8, 12, 16))

    def test_function_tuple_points_with_first_arg_that_not_func_negative(self):
        """
        Negative test to check exception by passing wrong first argument in 'tuple_points'.
        """
        with self.assertRaises(ValueError) as raised_exception:
            triangle.tuple_points([4, 3, 1], (4, 8, 12, 16))
        self.assertEqual(raised_exception.exception.args[0], 'Object [4, 3, 1] is not callable')

    def test_function_tuple_points_with_second_arg_that_not_iterable_negative(self):
        """
         Negative test to check exception by passing wrong second argument in 'tuple_points'.
        """
        with self.assertRaises(ValueError) as raised_exception:
            triangle.tuple_points(lambda x: x*4, 12)
        self.assertEqual(raised_exception.exception.args[0],'Object 12 is not iterable')

    @unittest.mock.patch('builtins.input', side_effect=['1', '3'])
    def test_function_parse_input_on_correct_value(self, input):
        """
        Test to function with input works fine.
        """
        point = triangle.parse_input('A')
        self.assertEqual(point,(1.0, 3.0))

    @unittest.mock.patch('builtins.input', side_effect=['1', ''])
    def test_function_parse_input_on_incorrect_value_with_whitespace_negatice(self, input):
        """
        Negative test to check exception by putting whitespace as input values.
        And check correct output.
        """
        with self.assertRaises(SystemExit) as raised_exception:
            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            triangle.parse_input('A')
            sys.stdout = sys.__stdout__
        self.assertEqual(capturedOut.getvalue(),
                         "Cannot convert '' to float. Coordinat value must be a number.\n")
        self.assertEqual(raised_exception.exception.args[0], 1)

    @unittest.mock.patch('builtins.input', side_effect=['a', ''])
    def test_function_parse_input_on_incorrect_value_with_string_negative(self, input):
        """
        Negative test to check exception by putting string as input values.
        And check correct output.
        """
        with self.assertRaises(SystemExit) as raised_exception:
            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            triangle.parse_input('A')
            sys.stdout = sys.__stdout__
        self.assertEqual(capturedOut.getvalue(),
                         "Cannot convert 'a' to float. Coordinat value must be a number.\n")
        self.assertEqual(raised_exception.exception.args[0], 1)

    @unittest.mock.patch('builtins.input', side_effect=['1,2,3', '4'])
    def test_function_parse_input_on_incorrect_value_with_tuple_negative(self, input):
        """
        Negative test to check exception by putting value that cannot be convert in float.
        And check correct output.
        """
        with self.assertRaises(SystemExit) as raised_exception:
            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            triangle.parse_input('A')
            sys.stdout = sys.__stdout__
        self.assertEqual(capturedOut.getvalue(),
                         "Cannot convert '1,2,3' to float. Coordinat value must be a number.\n")
        self.assertEqual(raised_exception.exception.args[0], 1)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_function_show_name(self,mock_stdout):
        """
        Test to check output of function.
        """
        triangle.show_program_name()
        self.assertEqual(mock_stdout.getvalue(),'Вычисление площади Герона по координатам.\n')

    @unittest.mock.patch('builtins.input', side_effect=['7', '1', '1', '9', '1', '1'])
    def test_function_main_work_with_correct_input(self, input):
        """
        Test to check main function works.
        """
        return_value = triangle.main(triangle.parse_input,triangle.Triangle.apex_of_triangle)
        self.assertEqual(return_value, 'Площадь треуголиника равна : 24.0')

    @unittest.mock.patch('builtins.input', side_effect=['1', '3', '1', '9', '1', '1'])
    def test_function_main_try_to_raise_some_exception_that_verified_above_negative(self, input):
        """
        Example that all tests above works fine.
        """
        with self.assertRaises(SystemExit) as raised_exception:
            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            return_value = triangle.main(triangle.parse_input, triangle.Triangle.apex_of_triangle)
            sys.stdout = sys.__stdout__
        self.assertEqual(capturedOut.getvalue(),
                          'Вычисление площади Герона по координатам.\n'
                          'Points ((1.0, 3.0), (1.0, 9.0), (1.0, 1.0)) do not form a triangle\n')


if __name__ == '__main__':
    unittest.main()
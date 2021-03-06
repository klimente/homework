"""
Unittests for triangle module
"""
import io
import unittest
import sys
import builtins
import unittest.mock

import triangle


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
        self.assertEqual(self.tr1.point_a, (7.0, 1.0), "Attribute of instance did not set")
        self.assertEqual(self.tr1.point_b, (1.0, 9.0), "Attribute of instance did not set")
        self.assertEqual(self.tr1.point_c, (1.0, 1.0), "Attribute of instance did not set")
        self.assertEqual(self.tr1.len_ab, 10.0, "Attribute of instance did not set")
        self.assertEqual(self.tr1.len_ac, 6.0, "Attribute of instance did not set")
        self.assertEqual(self.tr1.len_bc, 8.0, "Attribute of instance did not set")
        self.assertEqual(self.tr2.point_a, (3.0, 0.0), 'Attribute of instance did not set')
        self.assertEqual(self.tr2.point_b, (0.0, 4.0), 'Attribute of instance did not set')
        self.assertEqual(self.tr2.point_c, (0.0, 0.0), 'Attribute of instance did not set')
        self.assertEqual(self.tr2.len_ab, 5.0, 'Attribute of instance did not set')
        self.assertEqual(self.tr2.len_ac, 3.0, 'Attribute of instance did not set')
        self.assertEqual(self.tr2.len_bc, 4.0, 'Attribute of instance did not set')


    def test_instance_of_triangle_with_coordinates_with_values_ne_2_negative(self):
        """
        Negative test to check exception by putting point with length not equal 2.
        """
        with self.assertRaises(TypeError) as raised_exception:
            triangle.Triangle((1, 2, 3), (2, (3,)), ('c', 5))
        self.assertEqual(raised_exception.exception.args[0], 'Coordinates must have only 2 values',
                         'Values of exception wrong')


    def test_instace_of_triangle_with_coordinates_that_not_tuples_negative(self):
        """
        Negative test to check exception by putting not correct type in __init__.
        """
        with self.assertRaises(TypeError) as raised_exception:
            triangle.Triangle((1, 2), [2, 3], [3, 4])
        self.assertEqual(raised_exception.exception.args[0], 'Coordinates must be in tuple',
                         'Values of exception wrong')

    def test_instance_of_triangle_with_values_of_coordinates_that_not_number_negative(self):
        """
        Negative test to check exception by putting not numeric values in coordinates.
        """
        with self.assertRaises(ValueError) as raised_exception:
            triangle.Triangle((1,2),(2,(3,)), ('c',5))
        self.assertEqual(raised_exception.exception.args[0], 'Coordinate value must be number',
                         'Values of exception wrong')

    def test_instance_of_triangle_with_coordinates_that_do_not_form_triangle_negative(self):
        """
        Negative test to check exception by putting incorrect coordinetes to form a triangle.
        And check correct output.
        """
        with self.assertRaises(ValueError) as raised_exception:
            triangle.Triangle((3.0, 0.0), (4.0, 0.0), (5.0, 0.0))
        self.assertEqual(raised_exception.exception.args[0],
                         'Points ((3.0, 0.0), (4.0, 0.0), (5.0, 0.0)) do not form a triangle',
                         'Values of exception wrong')

    def test_privat_method_of_triangle_length_calculate_with_2_or_more_same_points_negative(self):
        """
        Negative test to check exception by putting incorrect coordinates to form triangle.
        And check correct output.
        """
        with self.assertRaises(ValueError) as raised_exception:
            triangle.Triangle((3.0, 0.0), (0.0, 0.0), (0.0, 0.0))

        self.assertEqual(raised_exception.exception.args[0], 'Cannot form triangle. Because coordinates '
                                                             '((0.0, 0.0), (0.0, 0.0)) are the same',
                         'Values of exception wrong')


    def test_get_attribute_of_class_apex_of_triangle(self):
        """
        Test to check attribute of class Triangle.
        """
        self.assertEqual(triangle.Triangle.apex_of_triangle, ('A', 'B', 'C'),
                         'Attribute of class did not work')

    def test_property_points(self):
        """
        Test to check property points of Triangle calculated right.
        """
        self.assertEqual(self.tr1.points,((7, 1), (1, 9), (1, 1)), 'Property did not work')
        self.assertEqual(self.tr2.points,((3.0, 0.0), (0.0, 4.0), (0.0, 0.0)), 'Property did not work')
        self.assertEqual(self.floattest.points, ((3.3, 0.0), (0.2, 4.2), (0.0, 0.0)), 'Property did not work')

    def test_property_sides(self):
        """
        Test to check property  sides of Triangle calculated right.
        """
        self.assertEqual(self.tr1.sides, (10.0, 6.0, 8.0), 'Property did not work')
        self.assertEqual(self.tr2.sides, (5.0, 3.0, 4.0), 'Property did not work')


    def test_property_semiperimetr(self):
        """
        Test to check property semiperimetr calculated right.
        """
        self.assertEqual(self.tr1.semiperimeter, 12.0, 'Property did not work')
        self.assertEqual(self.tr2.semiperimeter, 6.0, 'Property did not work')
        self.assertAlmostEqual(self.floattest.semiperimeter, 6.362456,places=6, msg='Property did not work')


    def test_private_method_length_calculate(self):
        """
        Test to check private method '_length_calculate' of Triangle works fine.
        """
        self.assertEqual(self.tr1._length_calculate((self.tr1.point_a,self.tr1.point_c)), 6.0,
                         'Private method did not work')
        self.assertEqual(self.tr2._length_calculate((self.tr2.point_a,self.tr2.point_c)), 3.0,
                         'Private method did not work')


    def test_private_method__multipliers(self):
        """
        Test to check private method '_multipliers' of Triangle works fine.
        """
        self.assertEqual(self.tr1._multipliers(), (12.0, 2.0, 6.0, 4.0), 'Private method did not work')
        self.assertEqual(self.tr2._multipliers(), (6.0, 1.0, 3.0, 2.0), 'Private method did not work')

    def test_method_area_by_heron(self):
        """
        Test to check method 'area_by_heron' of Triangle works fine.
        """
        self.assertEqual(self.tr1.area_by_heron(), 24.0, 'Method did not work')
        self.assertEqual(self.tr2.area_by_heron(), 6.0), 'Method did not work'
        self.assertAlmostEqual(self.floattest.area_by_heron(), 6.929, delta=0.001, msg='Method did not work')


    @unittest.mock.patch('builtins.input', side_effect=['1', '3'])
    def test_function_parse_input_on_correct_value(self, input):
        """
        Test to function with input works fine.
        """
        point = triangle.parse_input('A')
        self.assertEqual(point, (1.0, 3.0), 'Function of parsing input did not work')

    @unittest.mock.patch('builtins.input', side_effect=['1', ''])
    def test_function_parse_input_on_incorrect_value_with_whitespace_negatice(self, input):
        """
        Negative test to check exception by putting whitespace as input values.
        And check correct output.
        """
        self.assertEqual(triangle.parse_input('A'), None, 'Values wrong')

    @unittest.mock.patch('builtins.input', side_effect=['a', ''])
    def test_function_parse_input_on_incorrect_value_with_string_negative(self, input):
        """
        Negative test to check exception by putting string as input values.
        And check correct output.
        """
        self.assertEqual(triangle.parse_input('A'), None, 'Values wrong')

    @unittest.mock.patch('builtins.input', side_effect=['1,2,3', '4'])
    def test_function_parse_input_on_incorrect_value_with_tuple_negative(self, input):
        """
        Negative test to check exception by putting value that cannot be convert in float.
        And check correct output.
        """
        self.assertEqual(triangle.parse_input('A'), None, 'Values wrong')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_function_show_name(self,mock_stdout):
        """
        Test to check output of function.
        """
        triangle.show_program_name()
        self.assertEqual(mock_stdout.getvalue(),'Вычисление площади Герона по координатам.\n',
                         'Print did not work')

    @unittest.mock.patch('builtins.input', side_effect=['7', '1', '1', '9', '1', '1'])
    def test_function_main_work_with_correct_input(self, input):
        """
        Test to check main function works.
        """
        return_value = triangle.main(triangle.parse_input,triangle.Triangle.apex_of_triangle)
        self.assertEqual(return_value, 'Площадь треуголиника равна : 24.0',
                         'Main function did not work')

    @unittest.mock.patch('builtins.input', side_effect=['1', '3', '1', '9', '1', '1'])
    def test_function_main_try_to_give_incorrec_value_negative(self, input):
        """
        Example that all tests above works fine.
        """
        capturedOut = io.StringIO()
        sys.stdout = capturedOut
        return_value = triangle.main(triangle.parse_input, triangle.Triangle.apex_of_triangle)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOut.getvalue(),
                          'Вычисление площади Герона по координатам.\n'
                          'Points ((1.0, 3.0), (1.0, 9.0), (1.0, 1.0)) do not form a triangle\n',
                         'Output did not work')
        self.assertEqual(return_value, ' ')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_function_main_try_to_return_whitespace_coordinate_wronge_negative(self, out):
        """
        Test with not givin value
        """
        with unittest.mock.patch('builtins.input', side_effect=['']) as fake_input:
            value = triangle.main(triangle.parse_input, triangle.Triangle.apex_of_triangle)
        self.assertEqual(value, ' ')


if __name__ == '__main__':
    unittest.main()

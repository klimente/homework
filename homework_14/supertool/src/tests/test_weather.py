import unittest
import unittest.mock
import io
from unittest.mock import patch
from supertool import weather


class TestWeather(unittest.TestCase):

    def test_get_coordinates_positive(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = [
                {
                    'lat': '60.143707',
                    'lon': '30.207806',
                    'display_name': 'Сертолово, Всеволожский район,'
                                    ' Ленинградская область, Северо-Западный федеральный округ,'
                                    ' 188650, '
                                    'РФ',
                    'class': 'place',
                    'type': 'town',
                }]
            result = weather.get_coordinates('Sertolovo')
        print(result)
        self.assertEqual(result, ('60.143707', '30.207806'),
                         '"get_coordinates" works wrong')


    def test_get_coordinates_try_negative(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value = None
            with self.assertRaises(weather.ResponseError) as raised_exception:
                weather.get_coordinates('Serolovo')
        self.assertEqual(raised_exception.exception.args[0],
                             f'Cannot get response from Nominatim api')


    def test_get_coordinates_if_state_negetive(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = []
            with self.assertRaises(weather.NominatimError) as raised_exception:
                weather.get_coordinates('Some place nowhere')
        self.assertEqual(raised_exception.exception.args[0],
                         f'Cannot find this place: Some place nowhere')


    def test_get_weather_by_coordinates_positive(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = {
                'coord': {'lon': 30.21, 'lat': 60.14},
                'weather': [{'main': 'Clear', 'description': 'clear sky'}],
                'main': {'temp': 13, 'pressure': 1023, 'humidity': 58},
                'wind': {'speed': 0.81, 'deg': 22.5045},
                'cod': 200
            }
            result = weather.get_weather_by_coordinates(('60.143707', '30.207806'),'weather')
        print(result)
        self.assertEqual(result,{
            'coord': {'lon': 30.21, 'lat': 60.14},
            'weather': [{'main': 'Clear', 'description': 'clear sky'}],
            'main': {'temp': 13, 'pressure': 1023, 'humidity': 58},
            'wind': {'speed': 0.81, 'deg': 22.5045},
            'cod': 200
        })


    def test_get_weather_by_coordinates_try_negative(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value = None
            with self.assertRaises(weather.ResponseError) as raised_exception:
                weather.get_weather_by_coordinates(('60.143707', '30.207806'), 'weather')
        self.assertEqual(raised_exception.exception.args[0],
                         'Cannot get response from OpenWeatherMap api')


    def test_get_weather_by_coordinates_if_state_negative(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = {'cod': '404'}
            with self.assertRaises(weather.OpenWeatherMapError) as raised_exception:
                weather.get_weather_by_coordinates(('0', '-'), 'weather')
        self.assertEqual(raised_exception.exception.args[0],
                         "Cannot find place by coordinates ('0', '-')")


    def test_get_weather_by_coordinates_wrong_mode(self):
        with self.assertRaises(ValueError) as raised_exception:
            weather.get_weather_by_coordinates(('0', '-'), 'wrongmode')
        self.assertEqual(raised_exception.exception.args[0],'mode must be "forecast" or "weather"')


    def test_get_weather(self):
        example_data = {
                             'coord': {'lon': 30.21, 'lat': 60.14},
                             'weather': [{'main': 'Clear', 'description': 'clear sky'}],
                             'main': {'temp': 13, 'pressure': 1023, 'humidity': 58},
                             'wind': {'speed': 0.81, 'deg': 22.5045},
                             'cod': 200
                         }
        self.assertEqual(weather.get_weather(example_data), {
            'Weather': example_data['weather'][0]['main'],
            'Description': example_data['weather'][0]['description'].title(),
            'Temperature,  Cel': example_data['main']['temp'],
            'Pressure, hPa': example_data['main']['pressure'],
            'Humidity, %': example_data['main']['humidity'],
            'Wind speed, m/s:': example_data['wind']['speed']
    })
        print(weather.get_weather(example_data))


    def test_get_pretty_nice_table_positive(self):
        with patch('supertool.weather.get_coordinates') as mocked_coordinates, \
                patch('supertool.weather.get_weather_by_coordinates') as mock_get_weather,\
                patch('supertool.weather.get_current_weather') as mock_get_curr,\
                patch('supertool.weather.get_weather') as mockgetdict :
            mocked_coordinates.return_value = ('60.143707', '30.207806')
            mock_get_weather.return_value = {
                "cod":"200","message":0.0082,
                "cnt":40,
                "list":[
                    {'dt_txt':'1 06:00:00'},
                    {'dt_txt':'2 15:00:00'},
                    {'dt_txt':'3 21:00:00'}
                ]}
            mockgetdict.return_value = dict(zip(('a','b','c'),(1,2,3)))
            mock_get_curr.return_value = 'Some data'
            result = weather.get_pretty_nice_table('Place')
        self.assertEqual(result, None)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_weather_for_all_day(self, mock_stdout):
        result = weather.weather_for_all_day([1,2,3],[1,2,3],[1,2,3],[1,2,3])
        self.assertEqual(mock_stdout.getvalue(), "\n".join(f' {x[0]:20}'.ljust(10) + '|' + f'{x[1]:4}'.rjust(20) + '|' +
                    f'{x[2]:4}'.rjust(20) + '|' + f'{x[3]:4}'.rjust(20)
                    for x in list(zip([1,2,3],[1,2,3],[1,2,3],[1,2,3]))) + '\n')
        self.assertEqual(result, None)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_current_weather(self, mock_std):
        example_data = {
                             'coord': {'lon': 30.21, 'lat': 60.14},
                             'weather': [{'main': 'Clear', 'description': 'clear sky'}],
                             'main': {'temp': 13, 'pressure': 1023, 'humidity': 58},
                             'wind': {'speed': 0.81, 'deg': 22.5045},
                             'cod': 200
                         }
        with patch('supertool.weather.get_weather_by_coordinates') as mock_weather:
            mock_weather.return_value = example_data
            result = weather.get_current_weather('12.05',('30','60'))
        self.assertEqual(mock_std.getvalue(),
                         'Today' + '\n12.05\n' + '\n'.join(f' {k:20}'.ljust(10) + '|' + f'{v:4}'.rjust(20) + '|'
                                             for k, v in weather.get_weather(example_data).items()) + '\n')
        self.assertEqual(result, None)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_day_time(self, mstd_out):
        result = weather.get_day_time('10')
        self.assertEqual(mstd_out.getvalue(),
                         ' '.join('10'.ljust(5) + 'Morning'.rjust(12) + 'Day'.rjust(9) + 'Evening'.rjust(11)) + '\n')
        self.assertEqual(result, None)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_board(self, mstd_out):
        result = weather.get_board()
        self.assertEqual(mstd_out.getvalue(), '-' * 85 + '\n')
        self.assertEqual(result, None)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_title(self, mstd_out):
        result = weather.get_table_title('Home')
        self.assertEqual(mstd_out.getvalue(), 'Weather in Home'.center(85) + '\n')
        self.assertEqual(result, None)


    def test_get_weather_all_day_negative(self):
        with self.assertRaises(ValueError) as raised_exception:
            weather.weather_for_all_day(('0', '-'), 'mode')
        self.assertEqual(raised_exception.exception.args[0],'must be 4 iterable objects')


    def test_get_coordinates_with_incorrect_input_negative(self):
        with self.assertRaises(TypeError) as raised_exception:
            weather.get_coordinates(5)
        self.assertEqual(raised_exception.exception.args[0], 'place must be str')


    def test_get_weather_by_coordinates_with_incorrect_input_negative(self):
        with self.assertRaises(TypeError) as raised_exception:
            weather.get_weather_by_coordinates(5,'weather')
        self.assertEqual(raised_exception.exception.args[0], 'coordinates must be tuple')


    def test_get_weather_bu_coordinates_with_incorrect_mode_negative(self):
        with self.assertRaises(TypeError) as raised_exception:
            weather.get_weather_by_coordinates(('3','2'), 6)
        self.assertEqual(raised_exception.exception.args[0], 'mode must be str')


    def test_get_weather_without_dict_negative(self):
        with self.assertRaises(TypeError) as raised_exception:
            weather.get_weather('reply must be dict')
        self.assertEqual(raised_exception.exception.args[0],'reply must be dict')


if __name__ == '__main__':
    unittest.main()
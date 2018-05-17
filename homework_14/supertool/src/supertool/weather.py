"""
Module to work with OpenWeatheMap API and Nominatim API.
"""
import requests
import json
import os

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

class ResponseError(Exception):
    """
    Exception for errors from invalid requests.
    """
    pass


class OpenWeatherMapError(Exception):
    """
    Exception for errors from OpenWeatherMap API.
    """
    pass


class NominatimError(Exception):
    """
    Exception for errors from Nominatim API.
    """
    pass


def get_coordinates(place):
    """
    Function to get coordinated of the place through Nominatim API.
    :param place: location on the Earth.
    :type place: str.
    :return: tuple -- of coordinates.
    :raises: TypeError, ResponseError, NominatimError
    """
    if not isinstance(place, str):
        raise TypeError('place must be str')

    url = "https://nominatim.openstreetmap.org/"

    querystring = {
        "format": "json",
        "q": place,
        "limit": "1"
    }

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "86842e90-a82f-45b1-bf89-270e723f9c26"
        }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        reply = response.json()
    except Exception:
        raise ResponseError('Cannot get response from Nominatim api')
    if reply:
        return reply[0]['lat'], reply[0]['lon']
    raise NominatimError(f"Cannot find this place: {place}")


def get_weather_by_coordinates(coordinates, mode):
    """
    Function to get data about weather
    by coordinates through OpenWeatherMap API.
    :param coordinates: location (lat and lon).
    :type coordinates: tuple.
    :param mode: parameter to the OpenWatherMap API.
    :type mode: str.
    :return: dict -- data of the weather.
    :raises: TypeError, ValueError, ResponseError, OpenWeatherMapError.
    """
    if not isinstance(coordinates, tuple):
        raise TypeError('coordinates must be tuple')
    if not isinstance(mode, str):
        raise TypeError('mode must be str')
    if mode not in ['forecast', 'weather']:
        raise ValueError('mode must be "forecast" or "weather"')

    with open(os.path.join(DISTRO_ROOT_PATH, 'config.json')) as js:
        data = json.load(js)

    url = f"http://api.openweathermap.org/data/2.5/{mode}"

    querystring = {
        "lat": coordinates[0],
        "lon": coordinates[1],
        "appid": data["appid"],
        'units': 'metric'
    }

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "023a5f78-5b69-44a1-8b7e-76a1b0764634"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        reply = response.json()
    except Exception:
        raise ResponseError('Cannot get response from OpenWeatherMap api')

    if reply['cod'] == '404':
        raise OpenWeatherMapError(f"Cannot find place by coordinates {coordinates}")
    return reply


def get_weather(reply):
    """
    Function to get main parameters of the weather.
    :param reply: all data about weather.
    :type reply: dict.
    :return: dict -- of important parameters.
    :raises: TypeError.
    """
    if not isinstance(reply, dict):
        raise TypeError("reply must be dict")
    return {
        'Weather':reply['weather'][0]['main'],
        'Description':reply['weather'][0]['description'].title(),
        'Temperature,  Cel': reply['main']['temp'],
        'Pressure, hPa': reply['main']['pressure'],
        'Humidity, %': reply['main']['humidity'],
        'Wind speed, m/s:': reply['wind']['speed'],
    }


def weather_for_all_day(*args):
    """
    Function to show weather for whole day in one object.
    :param args: parameters names and parameters itself.
    :param args: iterabele objects.
    :return: None.
    :raises ValueError.
    """
    if len(args) != 4:
        raise ValueError('must be 4 iterable objects')
    print("\n".join(f' {x[0]:20}'.ljust(10) + '|' + f'{x[1]:4}'.rjust(20) + '|' +
                    f'{x[2]:4}'.rjust(20) + '|' + f'{x[3]:4}'.rjust(20)
                    for x in list(zip(*args))))

def get_current_weather(date, coordinates):
    """
    Function to show weather to current day.
    :param date: date of today.
    :type date: str.
    :param coordinates: location(lat, lon)
    :type coordinates: tuple
    :return: None.
    """
    print('Today'.ljust(10) + 'Right Now'.rjust(32) + f'\n{date}\n' +
          '\n'.join(f' {k:20}'.ljust(10) + '|' + f'{v:4}'.rjust(20) + '|'
                    for k, v in get_weather(get_weather_by_coordinates(coordinates, 'weather')).items()))


def get_day_time(date):
    """
    Function to show time of the day.
    :param date: date of today.
    :type date: str.
    :return: None.
    """
    print(' '.join(f'{date}'.ljust(5) + 'Morning'.rjust(12) + 'Day'.rjust(9) + 'Evening'.rjust(11)))


def get_board():
    """
    Function to show board in the a table.
    :return: None
    """
    print('-' * 85)

def get_table_title(place):
    """
    Function to show title of a table.
    :param place:
    :return: None.
    """
    print(f'Weather in {place}'.center(85))


def get_pretty_nice_table(place):
    """
    Main function to show whole table.
    :param place: location.
    :type place: str.
    :return: None.
    """
    coordinates = get_coordinates(place)
    forecast_reply = get_weather_by_coordinates(coordinates, 'forecast')

    weather_data = []
    date = ''

    get_table_title(place)
    for day in forecast_reply['list']:
        data = get_weather(day)

        if day['dt_txt'].split()[1] in ['06:00:00', '15:00:00', '21:00:00']:
            weather_data.append(data.values())

            if date != day['dt_txt'].split()[0]:
                get_board()

                if date == '':
                    date = day['dt_txt'].split()[0]
                    get_current_weather(date, coordinates)
                    weather_data.clear()

                else:
                    date = day['dt_txt'].split()[0]
                    weather_data.clear()
                    weather_data.append(data.values())

            if len(weather_data) == 3:
                get_day_time(date)
                weather_for_all_day(data.keys(), *[x for x in weather_data])


if __name__ == '__main__':
    get_pretty_nice_table('Sertolovo')

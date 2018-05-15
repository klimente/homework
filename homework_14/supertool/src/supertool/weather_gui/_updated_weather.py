"""
Module to work with OpenWeatheMap API and Nominatim API.
"""
import requests


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

    url = f"http://api.openweathermap.org/data/2.5/{mode}"

    querystring = {
        "lat": coordinates[0],
        "lon": coordinates[1],
        "appid": "b4a9d8e16b916107e741f1e84440c660",
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
    return ("\n".join(f' {x[0]:20}'.ljust(10) + '|' + f'{x[1]:4}'.rjust(20) + '|' +
                    f'{x[2]:4}'.rjust(20) + '|' + f'{x[3]:4}'.rjust(20)
                    for x in list(zip(*args))))


def get_day_time():
    """
    Function to get time of the day.
    :return: list.
    """
    return ['Morning','Day','Evening']


def get_pretty_nice_table(place):
    """
    Function to get data for table in gui.
    :param place: location.
    :type place: str.
    :returns: tuple -- list of dates, list of tuples of values.
    """
    coordinates = get_coordinates(place)
    forecast_reply = get_weather_by_coordinates(coordinates, 'forecast')

    weather_data = []
    date = ''
    dates = []
    result = []
    for day in forecast_reply['list']:
        data = get_weather(day)

        if day['dt_txt'].split()[1] in ['06:00:00', '15:00:00', '21:00:00']:
            weather_data.append(data.values())
            if date != day['dt_txt'].split()[0]:

                if date == '':
                    date = day['dt_txt'].split()[0]
                    weather_data.clear()

                else:
                    date = day['dt_txt'].split()[0]
                    weather_data.clear()
                    weather_data.append(data.values())

            if len(weather_data) == 3:
                dates.append(date)
                result.append(zip(*[x for x in weather_data]))
    return dates, result


if __name__ == '__main__':
    get_pretty_nice_table('Sertolovo')


import matplotlib.pyplot as plt
from collections import Counter
from math import floor
from itertools import accumulate
from functools import wraps


def _data_validator(func):
    """
    Private function to validate positional arguments of data.

    :param func: function that needs validation.
    :type func: function.
    :return: function.
    :raises: TypeError, ValueError
    """
    @wraps(func)
    def inner(*args, **kwargs):
        """
        Some service function.
        """
        if not isinstance(args[0], (list, tuple)):
            raise TypeError("Data must be list type")
        if not all([isinstance(i, (list, tuple)) for i in args[0]]):
            raise ValueError('value in data must be list')
        if not isinstance(args[1], int):
            raise TypeError("Col num must be int")
        return func(*args,**kwargs)
    return inner


@_data_validator
def _replace_data(data, col_num, result, from_str=False):
    """
    Private function tha replace invalid data on mean.

    :param data: main data.
    :type data: list of list.
    :param col_num: number of column of data.
    :type col_num: int.
    :param result: parsed data without invalid data.
    :type result: list.
    :param from_str: is data a string numbers.
    :type from_str: bool.
    :return: list.
    """
    result_with_mean = []
    average = mean(result)
    for item in data:
        item = item[col_num].replace(" ", "") if from_str else item[col_num]
        try:
            result_with_mean.append(float(item))
        except ValueError:
            result_with_mean.append(average)
    return result_with_mean


@_data_validator
def get_numeric_column(data, col_num, missing_data=False):
    """
    Function to get specify data by number of column.

    :param data: main data.
    :type data: list of list.
    :param col_num: number of column of data.
    :type col_num: int.
    :param missing_data: include missing data.
    :type missing_data: bool
    :return: list.
    """
    result = [float(i[col_num]) for i in data if i[col_num] not in ['NA','N/A']]
    if not missing_data:
        return result
    else:
        return _replace_data(data, col_num, result)


@_data_validator
def convert_str_to_numeric(data, col_num, missing_data=False):
    """
    Function to get specify data by number of column.
    From string numeric data.

    :param data: main data.
    :type data: list of list.
    :param col_num: number of column of data.
    :type col_num: int.
    :param missing_data: include missing data.
    :type missing_data: bool
    :return: list.
    :raises: ValueError.
    """
    result = []
    for item in data:
        elem = item[col_num].replace(" ", "")
        try:
            result.append(float(elem))
        except ValueError:
            pass
    if not missing_data:
        return result
    else:
        return _replace_data(data, col_num, result, from_str=True)


def _validator(check_inner=False):
    """
    Decorator to validate arguments of functions.

    :param check_inner: include validation of inner values.
    :param check_inner: bool
    :return: decorator.
    :raises: TypeError, ValueError.
    """
    def decorator(func):
        """
        Decorator.
        """
        @wraps(func)
        def inner(*args, **kwargs):
            """
            Service function.
            """
            if not isinstance(args[0],(list, tuple)):
                raise TypeError('input type must be list')
            if check_inner:
                if not all([isinstance(i, (float, int)) for i in args[0]]):
                    raise ValueError('value in x must be numeric')
            return func(*args, **kwargs)
        return inner
    return decorator


@_validator()
def missing_data(x, data):
    """
    Function to get procantage of missing data.

    :param x: obtained data.
    :type x: list
    :param data: full data.
    :type data: list.
    :return: float.
    :raises: TypeError.
    """
    if not isinstance(data, list):
        raise TypeError('data type must be list')
    return 1 - len(x) / len(data)


@_validator(check_inner=True)
def mean(x):
    """
    Function to get mean of some list x.

    :param x: list of data.
    :type x: list
    :return: float.
    """
    return sum(x) / len(x)


@_validator(check_inner=True)
def median(x):
    """
    Function to get median of some list x.

    :param x: list of data.
    :type x: list.
    :return: value from list.
    """
    n = len(x)
    sorted_x = sorted(x)
    mid = n // 2
    if n % 2 == 1:
        return sorted_x[mid]
    else:
        return (sorted_x[mid - 1] + sorted_x[mid]) / 2


@_validator(check_inner=True)
def mode(x):
    """
    Function to get mode of some list x.

    :param x: list of data.
    :type x: list.
    :return: list.
    """
    counts = Counter(x)
    max_val = max(counts.values())
    return [k for k, count in counts.items() if count == max_val]


@_validator(check_inner=True)
def quantile(x, p):
    """
    Function to get quantile of some list x.

    :param x: list of data.
    :type x: list
    :param p: order quantile
    :type p: float.
    :return: value of x
    """
    if not isinstance(p, float):
        raise TypeError("p must be float")
    if p < 0 or p > 1:
        raise ValueError('p must be in range (0,1)')
    p_idx = int(p * len(x))
    return sorted(x)[p_idx]


@_validator()
def data_range(x):
    """
    Function to get range of some data of list x.

    :param x: list of data.
    :type x: list.
    :return: float or int.
    """
    return max(x) - min(x)


@_validator()
def box_plot(x):
    """
    Function to build box plot.

    :param x: list of data.
    :return: None.
    """
    plt.boxplot(x)


def variance(x):
    """
    Function to get variance of some list x.

    :param x: list of data.
    :type x: list.
    :return: float.
    """
    m = mean(x)
    return sum([(d - m) ** 2 for d in x]) / (len(x) - 1)


def std(x):
    """
    Function to get std of some list x.

    :param x: list of data.
    :type x: list.
    :return: float.
    """
    return variance(x) ** 0.5


@_validator(check_inner=True)
def _dot(x, y):
    """
    Private function to get composition of lists x, y.

    :param x: list of data.
    :type x: list.
    :param y: list of data.
    :type y: list.
    :return: float or int.
    :raises: ValueError.
    """
    if len(x) != len(y):
        raise ValueError('x and y must have the same size')
    return sum([i * j for i, j in zip(x, y)])


def covarience(x, y): #dot
    """
    Function to get covariance of lists x, y.

    :param x: list of data.
    :type x: list.
    :param y: list of data.
    :type y: list.
    :return: float.
    :raises: ValueError,TypeError
    """
    if not isinstance(y, list):
        raise TypeError('y type must be list')
    if not all([isinstance(i, (float, int)) for i in y]):
        raise ValueError('value in x must be numeric')
    m_x = mean(x)
    m_y = mean(y)
    dev_x = [i - m_x for i in x]
    dev_y = [i - m_y for i in y]
    return _dot(dev_x, dev_y) / (len(x) - 1)


def correlation(x, y):
    """
    Function to get correlation of lists x, y.

    :param x: list of data.
    :type x: list.
    :param y: list of data.
    :type y: list.
    :return: float.
    """
    std_x = std(x)
    std_y = std(y)
    if std_x > 0 and std_y > 0:
        return covarience(x, y) / std_x / std_y
    return 0


@_validator()
def _make_buckets(x, bucket_size):
    """
    Private function to create buckets.
    :param x: list of data.
    :param bucket_size: bucket size.
    :type bucket_size: int.
    :return: Counter.
    """
    return Counter([bucket_size * floor(i / bucket_size) for i in x])


@_validator()
def hist(x, bucket_size, title=""):
    """
    Function to built histogtam.

    :param x: list of data.
    :param bucket_size: bucket size
    :type bucket_size: int.
    :param title: name of plot.
    :param title: str.
    :return: None.
    """
    hist_data = _make_buckets(x, bucket_size)
    plt.bar(hist_data.keys(), hist_data.values(), width=bucket_size,)
    plt.title(title)
    plt.show()


def just_plot(x, y, x_label = '', y_label='', title=''):
    """
    Function to built plot.

    :param x: list of data.
    :param y: list of data.
    :type y: list.
    :param bucket_size: bucket size
    :type bucket_size: int.
    :param title: name of plot.
    :type title: str.
    :param x_label: label for x axis.
    :type x_label: str
    :param y_label: label for y axis.
    :type y_label: str
    :return: None.
    """
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


@_validator()
def pdf(x):
    """
    Function to get probability density function of some list x.

    :param x: list of data.
    :type x: list.
    :return: dict.
    """
    size = len(x)
    return {key: value / size for key, value in Counter(x).items()}


@_validator()
def cdf(x):
    """
    Cumulative distribution function of list x.

    :param x: list of data.
    :return: dict.
    """
    size = len(x)
    frequency = Counter(x)
    return {key: value / size
            for key, value in zip(frequency.keys(), accumulate(frequency.values()))}

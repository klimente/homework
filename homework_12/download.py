#!/usr/bin/env python3.6

"""
Module to download images from external list of urls in multithreading way
and transform it to thumbnails with given parameters
and save it in given directory.
"""
import urllib.request
from io import BytesIO
import os
from multiprocessing.pool import ThreadPool
import time
import threading
import argparse

from PIL import Image

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
report_data = dict(zip(('success', 'failure', 'bytes_downloaded'), (0, 0, 0)))


def get_urls(source):
    """
    Function to validate and get list of urls by path.

    :param source: name of a file with urls.
    :param source: str.
    :return: list -- of strings (urls).
    :raises: FileNotFoundError.
    """
    if not os.path.exists(source):
        raise FileNotFoundError(f'no such file: {source}')
    with open(source, 'r') as file:
        return file.readlines()


def size_handle(arg_size):
    """
    Function to validate and get size of image.

    :param arg_size: parsing argument of the final file.
    :type arg_size: str.
    :return: tuple -- of sizes.
    :raises: ValueError
    """
    if 'x' not in arg_size:
        raise ValueError('size must include "x" between numerics')
    sizes = arg_size.split('x')
    if not sizes != 2:
        raise ValueError('size must have only two parametrs')
    size_w, size_h = tuple(sizes)
    if not all((size_w.isdecimal(), size_h.isdecimal())):
        raise ValueError('sizes must be digital')
    return int(size_w), int(size_h)


def threads_handle(arg_threads):
    """
    Function to validate and get number of threads.

    :param arg_threads: parsing argument of count of threads.
    :type arg_threads:  int
    :return: int -- number of threads
    :raises: ValueError
    """
    if not arg_threads > 0:
        raise ValueError('threads must be positive')
    return arg_threads


def target_direction_handle(arg_dir):
    """
    Function to check target directory.

    :param arg_dir: parsing argument of target directory.
    :type arg_dir: str
    :return: str
    """
    if not os.path.exists(arg_dir):
        os.mkdir(arg_dir)
    return arg_dir


def read_image(url):
    """
    Function to read image by url.
    :param url: source url of a image.
    :type url: str.
    :return: bytes - representation of image.
    """
    return urllib.request.urlopen(url).read()


def image_handler(params):
    """
    Function to handle image from urls list and save it.

    :param params: dict of parameters (index, url, size, target direction)
    :type params: dict
    :returns: None
    """
    try:
        im_bytes = read_image(params['url'])
        im = Image.open(BytesIO(im_bytes))
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.thumbnail(params["size"])
        im.save(os.path.join(params["target_dir"], params["index"].zfill(5) + '.jpeg'), 'JPEG')
        with threading.Lock():
            report_data['success'] += 1
            report_data['bytes_downloaded'] += len(im_bytes)
        print(f'url {params["index"]} successfully completed')
    except Exception as exc:
        if exc.args:
            print(f'url {params["index"]} failed with error: {type(exc).__name__}: {exc.args[0]}')
        else:
            print(f'url {params["index"]} failed with error: {type(exc).__name__}')
        with threading.Lock():
            report_data['failure'] += 1


def get_report(starts_time):
    """
    Function to create final report about execution of the program.
    :param starts_time: time of the start program.
    :type starts_time: float.
    :return: str -- report.
    """
    final_time = time.time() - starts_time
    return ('\nStatistic:\n' + f'number of successful downloads: {report_data["success"]}\n'
            + f'bytes download: {report_data["bytes_downloaded"]}\n'
            + f'number of failure: {report_data["failure"]}\n'
            + f'time spent(in seconds): {final_time}\n')


def threadings_process(urls_list, destanation, threads, size):
    """
    Function to create multithreading to handle images.

    :param urls_list: list of urls.
    :type urls_list: list .
    :param destanation: target path.
    :type destanation: str
    :param threads: number of threads.
    :type threads: int.
    :param size: size of a thumbnail.
    :type size: tuple.
    :return: None.
    """
    start = time.time()
    pol = ThreadPool(threads)
    pol.map(image_handler, tuple(dict(zip(('index', 'url', 'size', 'target_dir'),
                                          (str(index), url, size, destanation)))
                                 for index, url in enumerate(urls_list)))
    pol.close()
    pol.join()
    print(get_report(start))


def get_validate_args():
    """
    Function to parse console input and return validated values.

    :return: tuple -- of the validated parameters.
    """
    parser = argparse.ArgumentParser(description='Util to download, '
                                                 'handle and save image from txt file')
    parser.add_argument('source', type=str,
                        help='path to urls file')
    parser.add_argument('--dir', type=str,
                        help='target directory(def: current dir)', default=ABS_PATH)
    parser.add_argument('--threads', type=int,
                        help='threads number(def: 1) ', default=1)
    parser.add_argument('--size', type=str,
                        help='img size as a string(def: 100x100)', default='100x100')
    args = parser.parse_args()
    return get_urls(args.source), target_direction_handle(args.dir), threads_handle(args.threads), size_handle(args.size)


if __name__ == '__main__':
    try:
        threadings_process(*get_validate_args())
    except Exception as exc:
        print(f'error {type(exc).__name__}: {exc.args[0]}')

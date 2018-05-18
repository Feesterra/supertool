"""Поиск одинаковых файлов"""

import os

import hashlib


hashes = {}


def get_full_filenames(path):
    """Возвращает полный путь до каждого файла в директории path

    :param path: директория, в которой будет производиться поиск одинаковых по содержимому файлов
    """

    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(root, filename)


def get_md5(filename):
    """Читает файл и вычисляет MD5

    :param filename: полный путь до файла
    :return md5: хэш от содержимого файла
    """

    with open(filename, mode='rb') as file_to_check:
        data = file_to_check.read()
        md5 = hashlib.md5(data).hexdigest()
    return md5


def print_similar():
    """Выводит на консоль количество одинаковых файлов (не по названию, а по содержимому) и их пути"""

    count = 0

    for key, value in hashes.items():
        if len(value) > 1:
            count += 1
            return 'Найдено одинаковых файлов: \n{} штук:\t{}'.format(len(value), ', '.join(value))
    if count == 0:
        return 'Одинаковых файлов не найдено.'


def find_duplicates(path):
    """Проверяет существование запрашиваемого пути, сравнивает хэши всех файлов в директории path

    :param path: директория, в которой производится поиск
    """

    if os.path.exists(path):
        if not hashes:
            for filename in get_full_filenames(path):
                hash = get_md5(filename)
                if hash not in hashes.keys():
                    hashes[hash] = [filename]
                else:
                    hashes[hash].append(filename)
            return print_similar()
    else:
        raise Exception('{} неверный путь'.format(path))


import unittest

import supertool.work as work


class TestSupertool(unittest.TestCase):
    def test_get_full_filenames_positive(self):
        """Тестирует работу функции get_full_filenames"""


        self.assertEqual(['/home/sh/check/file2.txt', '/home/sh/check/tram/file1.txt'], \
                         list(work.get_full_filenames('/home/sh/check')))

    def test_get_md5_positive(self):
        """Тестирует работу функции get_md5"""

        self.assertEqual('d1bf8fc6af9166875316587ad697a719', work.get_md5('/home/sh/checking/second.txt'))

    def test_find_duplicates_negative(self):
        """Тестирует работу функции find_duplicates"""

        with self.assertRaises(Exception) as raised_exception:
            work.find_duplicates('/home/sh/checki')
            self.assertEqual('/home/sh/checki неверный путь', raised_exception.exception.args[0])

if __name__ == '__main__':
    unittest.main()
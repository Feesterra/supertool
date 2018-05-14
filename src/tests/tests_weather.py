import unittest

import supertool.weather as weather

class TestSupertoolWeather(unittest.TestCase):

    def test_nominatim_weather_daily_negative_1(self):
        """Tests function nominatim_weather_daily for raising error (location not found)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.nominatim_weather_daily('bla157ljiia', token_id='1b0ca47d89658cde3cc64234f71e0fc7', cnt=14)
            self.assertEqual('no such location found!', raised_exception.exception.args[0])

    def test_nominatim_weather_daily_negative_2(self):
        """Tests function nominatim_weather_daily for raising error (incorrect days)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.nominatim_weather_daily('London', token_id='1b0ca47d89658cde3cc64234f71e0fc7', cnt=44)
            self.assertEqual('Weather forecast may be provided for up to 16 days', raised_exception.exception.args[0])

    def test_nominatim_weather_daily_negative_3(self):
        """Tests function nominatim_weather_daily for raising error (token id)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.nominatim_weather_daily('London', token_id='aaa', cnt=10)
            self.assertEqual('You have inputted invalid token id!', raised_exception.exception.args[0])

    def test_nominatim_weather_negative_1(self):
        """Tests function nominatim_weather for raising error (token id)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.nominatim_weather('London', token_id='aaa')
            self.assertEqual('You have inputted invalid token id!', raised_exception.exception.args[0])

    def test_nominatim_weather_negative_2(self):
        """Tests function nominatim_weather for raising error (location)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.nominatim_weather_daily('bla157ljiia', token_id='1b0ca47d89658cde3cc64234f71e0fc7')
            self.assertEqual('no such location found!', raised_exception.exception.args[0])

    def test_weather_forecast_negative_1(self):
        """Tests function weather_forecast for raising error (location)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.weather_forecast('bla157ljiia', token_id='1b0ca47d89658cde3cc64234f71e0fc7')
            self.assertEqual('Input location name correctly!', raised_exception.exception.args[0])

    def test_weather_forecast__negative_2(self):
        """Tests function weather_forecast for raising error (location)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.weather_forecast('London', token_id='aaa')
            self.assertEqual('You have inputted invalid token id!', raised_exception.exception.args[0])

    def test_weather_negative_1(self):
        """Tests function weather for raising error (location)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.weather('London', token_id='aaa')
            self.assertEqual('You have inputted invalid token id!', raised_exception.exception.args[0])

    def test_weather_negative_2(self):
        """Tests function weather for raising error (token id)"""

        with self.assertRaises(Exception) as raised_exception:
            weather.weather('bla157ljiia', token_id='1b0ca47d89658cde3cc64234f71e0fc7')
            self.assertEqual('Input location name correctly!', raised_exception.exception.args[0])

    def test_kelv_to_cels_positive(self):
        self.assertEqual(0.15, float('{:.2}'.format(weather.kelv_to_cels(273.30))))



if __name__ == '__main__':
    unittest.main()
import weather
import unittest

class TestWeather(unittest.TestCase): 

    def setUp(self):
        self.valid_months = [num for num in range(1, 13)]

    def test_cels_to_far(self):
        self.assertEqual(weather.celsius_to_fahrenheit(0), 32)
        self.assertEqual(weather.celsius_to_fahrenheit(100), 212)
        self.assertNotEqual(weather.celsius_to_fahrenheit(99), 213)

    def test_is_hot(self):
        self.assertTrue(weather.is_hot(31))
        #self.assertTrue(weather.is_hot(30)) # TODO-> bug; will fix
        #self.assertFalse(weather.is_hot(30)) # TODO-> bug; will fix
        self.assertFalse(weather.is_hot(29))

    def test_get_season(self):
        self.assertEqual(weather.get_season(2), "winter")
        self.assertNotEqual(weather.get_season(3), "winter")
        self.assertEqual(weather.get_season(7), "summer")
        self.assertNotEqual(weather.get_season(11), "summer")

        with self.assertRaises(ValueError):
            weather.get_season(13)

        with self.assertRaises(ValueError):
            weather.get_season(0)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

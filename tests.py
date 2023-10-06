import unittest
import conversions as c


class ConversionsKnownValues(unittest.TestCase):
    """Tests conversion functions in conversions.py"""
    known_values = (
        (10.00, 50.00, 283.15),
        (20.00, 68.00, 293.15),
        (30.00, 86.00, 303.15),
        (40.00, 104.00, 313.15),
        (50.00, 122.00, 323.15),
        (60.00, 140.00, 333.15)
    )

    def testConvertCelsiusToKelvin(self):
        """Tests that convertCelsiusToKelvin returns the expected value."""
        for val in self.known_values:
            from_val = val[0]
            expected_val = val[2]
            returned_val = c.convertCelsiusToKelvin(from_val)
            self.assertEqual(returned_val,
                             expected_val,
                             msg=(
                                 '{}º Kelvin is not equal to expected value'
                                 ' of {}º Kelvin.') \
                             .format(returned_val, expected_val)
                             )

    def testConvertCelsiusToFahrenheit(self):
        """Tests that convertCelsiusToFahrenheit returns the expected value."""
        for val in self.known_values:
            from_val = val[0]
            expected_val = val[1]
            returned_val = c.convertCelsiusToFahrenheit(from_val)
            self.assertEqual(returned_val,
                             expected_val,
                             msg=(
                                 '{}º Fahrenheit is not equal to expected value'
                                 ' of {}º Fahrenheit.') \
                             .format(returned_val, expected_val)
                             )

    def testConvertFahrenheitToKelvin(self):
        """Tests that convertFahrenheitToKelvin returns the expected value."""
        for val in self.known_values:
            from_val = val[1]
            expected_val = val[2]
            returned_val = c.convertFahrenheitToKelvin(from_val)
            self.assertEqual(returned_val,
                             expected_val,
                             msg=(
                                 '{}º Kelvin is not equal to expected value'
                                 ' of {}º Kelvin.') \
                             .format(returned_val, expected_val)
                             )

    def testConvertFahrenheitToCelsius(self):
        """Tests that convertFahrenheitToCelsius returns the expected value."""
        for val in self.known_values:
            from_val = val[1]
            expected_val = val[0]
            returned_val = c.convertFahrenheitToCelsius(from_val)
            self.assertEqual(returned_val,
                             expected_val,
                             msg=(
                                 '{}º Celsius is not equal to expected value'
                                 ' of {}º Celsius.') \
                             .format(returned_val, expected_val)
                             )

    def testConvertKelvinToFahrenheit(self):
        """Tests that convertKelvinToFahrenheit returns the expected value."""
        for val in self.known_values:
            from_val = val[2]
            expected_val = val[1]
            returned_val = c.convertKelvinToFahrenheit(from_val)
            self.assertEqual(returned_val,
                             expected_val,
                             msg=(
                                 '{}º Fahrenheit is not equal to expected value'
                                 ' of {}º Fahrenheit.') \
                             .format(returned_val, expected_val)
                             )

    def testConvertKelvinToCelsius(self):
        """Tests that convertKelvinToCelsius returns the expected value."""
        for val in self.known_values:
            from_val = val[2]
            expected_val = val[0]
            returned_val = c.convertKelvinToCelsius(from_val)
            self.assertEqual(returned_val,
                             expected_val,
                             msg=(
                                 '{}º Celsius is not equal to expected value'
                                 ' of {}º Celsius.') \
                             .format(returned_val, expected_val)
                             )


class ConversionsRefactoredKnownValues(unittest.TestCase):
    """Tests convert function in conversions_refactored.py"""
    known_values = (
        ('celsius', 'kelvin', 0.00, 273.15),
        ('celsius', 'fahrenheit', 32.00, 89.60),
        ('fahrenheit', 'kelvin', 118.40, 321.15),
        ('fahrenheit', 'celsius', 212.00, 100.00),
        ('kelvin', 'celsius', 0.00, -273.15),
        ('kelvin', 'fahrenheit', -100.00, -639.67),
        ('miles', 'yards', 1.00, 1760.00),
        ('miles', 'meters', 2.00, 3218.69),
        ('miles', 'feet', 2.00, 10560.00),
        ('yards', 'miles', 6000.00, 3.41),
        ('yards', 'meters', 300.00, 274.22),
        ('yards', 'feet', 120.00, 360.00),
        ('meters', 'miles', 60000.00, 37.28),
        ('meters', 'yards', 150.00, 164.10),
        ('meters', 'feet', 157.00, 515.12),
        ('feet', 'miles', 2640.00, 0.50),
        ('feet', 'yards', 9000.00, 3000.00),
        ('feet', 'meters', 100000.00, 30478.51)
    )

    def testConvert(self):
        """Tests that convert returns the expected value."""
        for val in self.known_values:
            from_unit = val[0]
            to_unit = val[1]
            from_val = val[2]
            expected_val = val[3]


if __name__ == '__main__':
    unittest.main()
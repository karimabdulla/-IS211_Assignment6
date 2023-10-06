def convertCelsiusToKelvin(value):
    """ Converts Celsius to Kelvin.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Kelvin.

    Example:
        >>> convertCelsiusToKelvin(30.0)
        303.15
   """

    return round((float(value) + 273.15), 2)


def convertCelsiusToFahrenheit(value):
    """Converts Celsius to Fahrenheit.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Fahrenheit.

    Example:
        >>> convertCelsiusToFahrenheit(30)
        86.0
    """

    return round(((float(value) * 1.8) + 32), 2)


def convertFahrenheitToKelvin(value):
    """This function converts from Fahrenheit to Kelvin.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Kelvin.

    Example:
        >>> convertFahrenheitToKelvin(50)
        283.15
    """

    return round(((float(value) + 459.67) * 0.5555555556), 2)


def convertFahrenheitToCelsius(value):
    """This function converts from Fahrenheit to Celsius.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Celsius.

    Example:
        >>> convertFahrenheitToCelsius(50)
        10.0
    """

    return round(((float(value) - 32.0) * 0.5555555556), 2)


def convertKelvinToFahrenheit(value):
    """This function converts from Kelvin to Fahrenheit.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Fahrenheit.

    Example:
        >>> convertKelvinToFahrenheit(503.15)
        446.0
    """

    return round(((float(value) * 1.8) - 459.67), 2)


def convertKelvinToCelsius(value):
    """This function converts from Kelvin to Celsius.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Celsius.

    Example:
        >>> convertKelvinToCelsius(503.15)
        230.0
    """

    return round((float(value) - 273.15), 2)
import datetime

import reader.bme280 as bme280

PRESSURE_AT_SEA_LEVEL = 1013.25
STANDARD_LAPSE_RATE = 0.0065


def calculateAltitudeFromHypsometric(currentPressure, currentCelsius):
    # See Hypsometric Equation for more information
    current_kelvin = currentCelsius + 273.15
    numerator = ((PRESSURE_AT_SEA_LEVEL / currentPressure) ** (1 / 5.257) - 1) * current_kelvin
    return numerator / STANDARD_LAPSE_RATE


def getTimestamp():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def readAtpData():
    temperature, pressure, humidity = bme280.readBME280All()
    return temperature, pressure, calculateAltitudeFromHypsometric(pressure, temperature), getTimestamp()

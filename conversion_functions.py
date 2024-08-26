def fahrenheit_to_celcius(temperature: int) -> int:
    return round((temperature - 32) * 5 / 9)


def celcius_to_fahrenheit(temperature: int) -> int:
    return round((temperature * 9 / 5) + 32)

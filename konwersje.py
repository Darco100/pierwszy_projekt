"""Funkcje do przeliczania temperatur."""


def c_na_f(celsjusz: float) -> float:
    """Zamienia stopnie Celsjusza na Fahrenheita."""
    return celsjusz * 9 / 5 + 32


def f_na_c(fahrenheit: float) -> float:
    """Zamienia stopnie Fahrenheita na Celsjusza."""
    return (fahrenheit - 32) * 5 / 9
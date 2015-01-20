from currency_convert import *

rates = [("USD", "EUR", .74), ("EUR", "JPY", 145.949)]

def test_convert_match():
    assert convert(rates, 1, "USD", "USD") == 1

def test_convert_doleur():
    assert convert(rates, 1, "USD", "EUR") == .74

def test_convert_eurdol():
    assert convert(rates, 1, "EUR", "USD") == 1.35

def test_convertEURJPY():
    assert convert(rates, 1, "EUR", "JPY") == 145.95

def test_convertJPYEUR():
    assert convert(rates, 1, "JPY", "EUR") == .01

def test_rate_pull():
    assert get_rate(rates, "USD", "EUR") == .74
    assert get_rate(rates, "EUR", "USD") == 1.35
    assert get_rate(rates, "JPY", "EUR") == .01
    assert get_rate(rates, "EUR", "JPY") == 145.95

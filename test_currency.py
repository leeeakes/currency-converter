from currency_convert import *

rates = [("USD", "EUR", .74)]

def test_convert_match():
    assert convert(rates, 1, "USD", "USD") == 1

def test_convert_doleur():
    assert convert(rates, 1, "USD", "EUR") == .74

def test_convert_eurdol():
    assert convert(rates, 1, "EUR", "USD") == 1.35

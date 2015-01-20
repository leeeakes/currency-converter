from currency_convert import *

rates = [("USD", "EUR", 1.25)]

def test_convert_match():
    assert convert(2, 1, "COC", "COC") == 1

def test_convert_rate():
    assert convert(2, 1, "USD", "COC") == 2
    assert convert(.75, 1.5, "USD", "COC") == 1.12

#def convert(rates, value, orig_cur, new_cur):
#    if orig_cur == new_cur:
#        return value
#    conversion = value * rates
#    return conversion

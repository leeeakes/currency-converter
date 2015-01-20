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




#    assert convert(rates, 1, "EUR", "JPY") == ("EUR", "JPY", 145.949)

#print(convert(rates, 1, "EUR", "JPY"))
#print(convert(rates, 1, "JPY", "EUR"))
#print(convert(rates, 1, "EUR", "USD"))
#print(convert(rates, 1, "USD", "EUR"))

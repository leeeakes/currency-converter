#RATES list should be a list of tuples, with each tuple containing a currency
#code you can convert from, a currency code you can convert to, and a rate.

def convert(rates, value, orig_cur, new_cur):
    if orig_cur == new_cur:
        return value
    conversion = conversion = round(value * rates[0][2], 2)
    return conversion

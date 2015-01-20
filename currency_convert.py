#RATES list should be a list of tuples, with each tuple containing a currency
#code you can convert from, a currency code you can convert to, and a rate.

def convert(rates, value, orig_cur, new_cur):
    if orig_cur == new_cur:
        return value
    elif orig_cur == rates[0][0]:
        conversion = round(value * rates[0][2], 2)
        return conversion
    elif orig_cur == rates[0][1]:
        conversion = round(value / rates[0][2], 2)
        return conversion



#onvert(rates, 1, "USD", "EUR")

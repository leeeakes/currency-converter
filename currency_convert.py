def get_rate(rates, orig_cur, new_cur):
    for rate in rates:
        if orig_cur in rate[0] and new_cur in rate[1]:
            conv = round(rate[2],2)
            return conv
        elif orig_cur in rate[1] and new_cur in rate[0]:
            conv = round(1 / rate[2],2)
            return conv

def convert(rates, value, orig_cur, new_cur):
    if orig_cur == new_cur:
        return value
    else:
        rate = get_rate(rates, orig_cur, new_cur)
        final = value * rate
        return rate

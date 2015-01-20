#RATES list should be a list of tuples, with each tuple containing a currency
#code you can convert from, a currency code you can convert to, and a rate.

rates = [("USD", "EUR", .74)]

def convert(rates, value, orig_cur, new_cur):
    if orig_cur == new_cur:
        return value
    conversion = value * rates
    return conversion

#def get_rate():


#Create a function called convert that takes
#a list called rates,
#a number called value,
#a string called from,
#and a string called to.

#rates = [("USD", "EUR", .74)]
#This means that each dollar is worth 0.74 euros.

#value is the amount of currency,
#from is the current currency code
#and to is the currency code you wish to convert to.

#Given the above rates, make sure that converting 1 dollar into euros
#returns the following value: 0.74.

#Make sure than when you call convert with from and to being equal,
#the return value is the same as value.


#USD to EUR,
#EUR to USD
#EUR to JPY
#JPY to EUR.

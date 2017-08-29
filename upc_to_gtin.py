import pandas as pd
from sys import argv
import numpy as np

codes = pd.read_excel(argv[1], converters = {'Inner 11 Digit': str})
print(codes)
upc_str = codes['Inner 11 Digit']
#upc_str = upc_str.apply(str)
#upc_str = upc_str.apply(lambda x: x.astype(str))
print(upc_str)
#string = '12312312312'
#retail_upc = []

def add_check_digit(upc_str):
    """
    Returns a 12 digit upc-a string from an 11-digit upc-a string by adding 
    a check digit
    >>> add_check_digit('02345600007')
    '023456000073'
    >>> add_check_digit('21234567899')
    '212345678992'
    >>> add_check_digit('04210000526')
    '042100005264'
    """

    if len(upc_str) != 11:
        return (np.nan, np.nan)

    odd_sum = 0
    even_sum = 0
    for i, char in enumerate(upc_str):
        j = i+1
        if j % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)

    total_sum = (odd_sum * 3) + even_sum
    mod = total_sum % 10
    check_digit = 10 - mod
    if check_digit == 10:
        check_digit = 0
    retail_upc = str(upc_str) + str(check_digit)
    return retail_upc, check_digit

print(upc_str.apply(lambda x: add_check_digit(x)))
#retail_upc = upc_str.apply(lambda x: add_check_digit(x))

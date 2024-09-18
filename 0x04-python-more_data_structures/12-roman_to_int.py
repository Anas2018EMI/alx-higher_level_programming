#!/usr/bin/python3
def roman_to_int(r_st):
    if not isinstance(r_st, str) or r_st is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    int_value = 0

    for i in range(len(r_st)):
        if i < len(r_st) - 1 and roman[r_st[i]] < roman[r_st[i + 1]]:
            int_value -= roman[r_st[i]]
        else:
            int_value += roman[r_st[i]]

    return int_value

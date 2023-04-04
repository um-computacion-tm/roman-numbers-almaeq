def roman_to_decimal(roman_numeral):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal_num = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i-1]]:
            decimal_num += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i-1]]
        else:
            decimal_num += roman_numerals[roman_numeral[i]]
    return decimal_num
    

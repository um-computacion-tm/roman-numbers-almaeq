# numeros romanos

def decimal_to_roman(decimal):
    total = ''
    
    if decimal == 1000:
        total += 'M'
    if 400 > decimal >= 100:
        centena = decimal // 100
        total += 'C' * centena
        decimal = decimal % 100 
    if 500 > decimal >= 400:
        total += "CD"
        decimal = decimal % 100
    if 900 > decimal >= 500:
        total += 'D'
        decimal -= 500
        centena = decimal //100
        total += 'C' * centena
        decimal = decimal % 100
    if 1000 > decimal >= 900:
        total += "CM"
        decimal = decimal % 100
    if 40 > decimal >= 10:
        decena = decimal // 10
        total += "X" * decena
        decimal = decimal % 10
    if 50 > decimal >= 40:
        total += "XL"
        decimal = decimal % 10
    if 90 > decimal >= 50:
        total += 'L' 
        decimal -= 50
        decena = decimal // 10
        total += "X" * decena
        decimal = decimal % 10
    if 100 > decimal >= 90:
        total += "XC"
        decimal = decimal % 10
    if decimal <= 3:
        total += 'I' * decimal
    if decimal == 4:
        total += "IV"
    elif 9 > decimal >= 5:
        total += 'V'
        decimal -= 5
        unidad = decimal % 10
        total += "I" * unidad
    elif decimal == 9:
        total += "IX"
    return total



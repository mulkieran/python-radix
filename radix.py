__author__ = 'Valeria'

symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def to_base_10(number, base):
    error = False
    result = 0
    figures = []
    number = str(number)
    number.lower()
    for k in number:
        i = symbol.index(k)
        if i >= base:
            error = True
        figures.append(i)
    for k in range(len(figures)):
        result += (figures[k]) * base**(len(figures)-k-1)
    result = str(result)
    if error:
        raise Exception('Not valid number')
    else:
        return result

def from_base_10(number, base):
    values = []
    try:
        number = int(number)
    except:
        raise Exception('Not valid number')
    while number > 0:
        remainder = number % base
        values.append(remainder)
        number = number/base
    result = ''
    for i in range(len(values)):
        result += symbol[values[len(values)-1-i]]
    return result

def new_radix(number, old_base = 10 , new_base = 10):
    if old_base != 10:
        number = to_base_10(number, old_base)
    if new_base != 10:
        number = from_base_10(number, new_base)
    return number
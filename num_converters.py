
def num_to_roman(num:int) -> str:
    """
    converts classical numbers (int) into roman numbers (str)
    example: 5 -> 'V'
    """
    roman_nbs = [
        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    ]

    result = ""
    for turn, n in enumerate(str(num), start=1):
        if n == '0':
            next
        else:
            result += roman_nbs[len(str(num))-turn][int(n)-1]
    return result

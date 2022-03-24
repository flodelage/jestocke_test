
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

    if len(str(num)) == 1:
        return roman_nbs[0][num-1]

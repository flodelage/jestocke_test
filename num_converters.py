
class RomanNumeralConverter:

    def num_to_roman(self, num: int) -> str:
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

    def roman_to_num(self, rom: str) -> int:
        """
        converts roman numbers (str) into classical numbers (int)
        example: 'V' -> 5
        """
        classical_nbs = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }

        result = 0
        turn = 0
        while turn < len(rom):
            try:
                if rom[turn] + rom[turn+1] in classical_nbs:
                    result += classical_nbs[rom[turn] + rom[turn+1]]
                    turn += 2
                else:
                    result += classical_nbs[rom[turn]]
                    turn += 1
            except IndexError:
                result += classical_nbs[rom[turn]]
                turn += 1
        return result

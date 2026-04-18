class Cipher:
    def process(self, text: str, shift: int) -> str:
        raise NotImplementedError()


class CaesarCipher(Cipher):
    def __init__(self):
        self.eng_lower = 'abcdefghijklmnopqrstuvwxyz'
        self.eng_upper = self.eng_lower.upper()

        self.rus_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.rus_upper = self.rus_lower.upper()

    def _shift_alphabet(self, char, alphabet, shift):
        idx = alphabet.find(char)
        if idx != -1:
            return alphabet[(idx + shift) % len(alphabet)]
        return None

    def process(self, text: str, shift: int) -> str:
        result = ""

        for char in text:
            # Английские буквы
            res = self._shift_alphabet(char, self.eng_lower, shift)
            if res:
                result += res
                continue

            res = self._shift_alphabet(char, self.eng_upper, shift)
            if res:
                result += res
                continue

            # Русские буквы
            res = self._shift_alphabet(char, self.rus_lower, shift)
            if res:
                result += res
                continue

            res = self._shift_alphabet(char, self.rus_upper, shift)
            if res:
                result += res
                continue

            # Цифры
            if char.isdigit():
                result += str((int(char) + shift) % 10)
            else:
                result += char

        return result
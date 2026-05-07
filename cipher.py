class Cipher:
    def process(self, text: str, key: str) -> str:
        raise NotImplementedError()


class VernamCipher(Cipher):
    def process(self, text, key):
        if not key:
            return "Введите ключ"

        result = []
        key_len = len(key)

        for i, ch in enumerate(text):
            k = ord(key[i % key_len])
            result.append(chr(ord(ch) ^ k))

        return ''.join(result)
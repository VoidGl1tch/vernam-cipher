from cipher import Cipher
from model import TextModel


class CipherController:
    def __init__(self, cipher: Cipher, model: TextModel):
        self._cipher = cipher
        self._model = model

    def encrypt(self, shift: int) -> str:
        return self._cipher.process(self._model.get_text(), shift)

    def decrypt(self, shift: int) -> str:
        return self._cipher.process(self._model.get_text(), -shift)
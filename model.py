class TextModel:
    def __init__(self):
        self._text = ""

    def set_text(self, text: str):
        self._text = text

    def get_text(self) -> str:
        return self._text
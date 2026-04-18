import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QPushButton, QHBoxLayout
)

from cipher import CaesarCipher
from model import TextModel
from controller import CipherController
from options_frame import OptionsFrame


class CipherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.model = TextModel()
        self.cipher = CaesarCipher()
        self.controller = CipherController(self.cipher, self.model)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Шифрователь Цезаря")

        layout = QVBoxLayout()

        self.input_text = QTextEdit()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.options = OptionsFrame()

        self.encrypt_btn = QPushButton("Зашифровать")
        self.decrypt_btn = QPushButton("Дешифровать")

        layout.addWidget(QLabel("Поле ввода:"))
        layout.addWidget(self.input_text)

        layout.addWidget(self.options)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.encrypt_btn)
        btn_layout.addWidget(self.decrypt_btn)
        layout.addLayout(btn_layout)

        layout.addWidget(QLabel("Поле вывода:"))
        layout.addWidget(self.output_text)

        self.setLayout(layout)

        self.encrypt_btn.clicked.connect(self.handle_encrypt)
        self.decrypt_btn.clicked.connect(self.handle_decrypt)

    def handle_encrypt(self):
        self.model.set_text(self.input_text.toPlainText())
        result = self.controller.encrypt(self.options.get_shift())
        self.output_text.setPlainText(result)

    def handle_decrypt(self):
        self.model.set_text(self.input_text.toPlainText())
        result = self.controller.decrypt(self.options.get_shift())
        self.output_text.setPlainText(result)


# ===================== Точка входа =====================
def main():
    app = QApplication(sys.argv)
    window = CipherApp()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

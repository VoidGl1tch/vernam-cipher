from PyQt6.QtWidgets import *
import random


class OptionsFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.key_field = QTextEdit()

        self.random_btn = QPushButton("Сгенерировать рандомный ключ")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ключ:"))
        layout.addWidget(self.key_field)
        layout.addWidget(self.random_btn)

        self.setLayout(layout)

        self.random_btn.clicked.connect(self.generate_random)

    def generate_random(self):
        s = ''
        for i in range(random.randint(3, 50)):
            s += chr(random.randint(40, 176))
        self.key_field.setText(s)


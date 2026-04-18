from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSpinBox, QPushButton
import random


class OptionsFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.shift_box = QSpinBox()
        self.shift_box.setRange(-100, 100)

        self.random_btn = QPushButton("Сгенерировать рандомный ключ")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ключ:"))
        layout.addWidget(self.shift_box)
        layout.addWidget(self.random_btn)

        self.setLayout(layout)

        self.random_btn.clicked.connect(self.generate_random)

    def generate_random(self):
        value = random.randint(-25, 25)
        self.shift_box.setValue(value)

    def get_shift(self) -> int:
        return self.shift_box.value()

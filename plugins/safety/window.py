from PyQt6.QtWidgets import (
        QWidget,
        QLabel
    )


class SafetyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = None
        QLabel("Safety Activity", self)

    def clicked(self):
        self.show()

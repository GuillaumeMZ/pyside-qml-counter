import sys
from pathlib import Path

from PySide6.QtCore import QObject, Property, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class Counter(QObject):
    def __init__(self):
        super().__init__()
        self._value = 0

    valueChanged = Signal(int)

    @Property(int, notify=valueChanged)
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: int):
        self._value = new_value
        self.valueChanged.emit(new_value)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    # The counter object is created BEFORE the QML engine so that its destructor is called after the QML engine's. This avoids "Cannot read property x of null" errors.
    counter = Counter()

    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"

    # The counter property is set BEFORE the QML file is loaded. Without this, we would see ReferenceErrors in the console.
    engine.rootContext().setContextProperty("counter", counter)

    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

import sys
from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("bybit_ui_v1.ui")
window.show()
app.exec()
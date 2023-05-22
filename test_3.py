from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtWidgets import QApplication, QTableView, QItemDelegate, QPushButton

class ButtonDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton("Botón", self.parent())

    def createEditor(self, parent, option, index):
        #return self.button
        if index.row() == 1 and index.column() == 0:  # Definir la celda específica (segunda fila, primera columna)
            return self.button


    def setEditorData(self, editor, index):
        pass

    def setModelData(self, editor, model, index):
        pass

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class TableModel(QAbstractTableModel):
    def __init__(self, data, header_labels, parent=None):
        super().__init__(parent)
        self._data = data
        self._header_labels = header_labels

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._header_labels)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return self._data[index.row()][index.column()]

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._header_labels[section]

        return None

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    data = [
        ['John', 25],
        ['Jane', 30],
        ['Alice', 35]
    ]
    header_labels = ['Name', 'Age']

    model = TableModel(data, header_labels)

    table_view = QTableView()
    table_view.setModel(model)
    table_view.setItemDelegateForColumn(0, ButtonDelegate(table_view))

    table_view.show()

    sys.exit(app.exec())

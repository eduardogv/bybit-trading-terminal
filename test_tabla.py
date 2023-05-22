import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout, QPushButton, QStyledItemDelegate, QItemDelegate

import pandas as pd
from open_orders import get_orders


class PandasModel(QAbstractTableModel):
    
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent):
        return self._data.shape[0]

    def columnCount(self, parent):
        return self._data.shape[1]

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])

        return None

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])
            elif orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

        return None


# Esta clase se usa en el metodo que me trae lag
class ButtonDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == 0:
            button = QPushButton("Botón", self.parent())
            button.setGeometry(option.rect)
            button.show()

        else:
            super().paint(painter, option, index)


# Este es el metodo bueno
class ButtonDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton("Botón", self.parent())

    def createEditor(self, parent, option, index):
        return self.button

    def setEditorData(self, editor, index):
        pass

    def setModelData(self, editor, model, index):
        pass

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)



if __name__ == '__main__':
    # Cargar los datos en un DataFrame de pandas
    #data = pd.DataFrame({'Columna1': [1, 2, 3], 'Columna2': ['A', 'B', 'C']})


    orders = get_orders()
    data = pd.DataFrame.from_dict(orders)
    data = data[["symbol", "price", "side", "takeProfit", "stopLoss"]]
    print(data)

    # Crear una instancia del modelo de datos y asignar el DataFrame
    model = PandasModel(data)

    # Crear una aplicación de PyQt6
    app = QApplication(sys.argv)

    # Crear una ventana principal de PyQt6
    window = QMainWindow()
    window.setWindowTitle('Tabla con DataFrame')

    # Crear una instancia de QTableView y asignar el modelo a la tabla
    table = QTableView()
    table.setModel(model) # AQUI SE ASIGNA EL MODELO AL TABLEVIEW
    table.setItemDelegateForColumn(2, ButtonDelegate(table)) # BOTON
    
    # Metodo que me trae lag a la UI
    #table.setItemDelegateForColumn(0, ButtonDelegate(table))

    # Establecer la tabla como el widget central de la ventana
    window.setCentralWidget(table)

    # Mostrar la ventana
    window.show()

    # Iniciar el bucle de eventos de la aplicación
    sys.exit(app.exec())

  

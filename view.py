from PyQt6 import QtCore, QtGui, QtWidgets
from ui.bybit_ui_v3 import Ui_MainWindow
from PyQt6.QtCore import QAbstractTableModel, Qt



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        #Se configura la GUI usando Qt designer
        self.setupUi(self)
    
    def set_orders(self, data):
        self.pandas_model = PandasModel(data)
        self.orders_table.setModel(self.pandas_model)

    def set_positions(self, data):
        try:
            self.pandas_model = PandasModel(data)
            self.positions_table.setModel(self.pandas_model)
        except:
            print("no data")

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
    


    # Método que muestra el cover en la GUI
    # def cover_img(self, image):
    #     cover_img = QtGui.QPixmap(image)
    #     self.cover_qlabel.setPixmap(cover_img)


    # Method to set columns width
    # def set_columns_width(self):
    #     self.tabla.setColumnWidth(0, 100) #Denominacion
    #     self.tabla.setColumnWidth(1, 100) #Especialidad
    #     self.tabla.setColumnWidth(2, 150) #Marca
    #     self.tabla.setColumnWidth(3, 200) #Modelo
    #     self.tabla.setColumnWidth(4, 220) #Descripcion
    #     self.tabla.setColumnWidth(5, 450) #Link



    # Metodo para definir el numero de filas de las tablas
    def define_rows(self, rows):
        #self.tabla.setRowCount(rows)
        pass

    



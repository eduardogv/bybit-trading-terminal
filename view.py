from PyQt6 import QtCore, QtGui, QtWidgets
from ui.bybit_ui_v3 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#class MainWindow(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        #Se configura la GUI usando Qt designer
        self.setupUi(self)

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

    # Method to print data in positions table


    # Method to print data in orders table



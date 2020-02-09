# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import struct
import time, threading

while(1):
    while(1):
        try:
            numero = str(int(input(">  COM: ")))
            port = "com" + numero
            break
        except:
            print ("Ingresar un valor numerico")
    try:
        data = serial.Serial(port, baudrate = 9600, timeout=1500)
        break
    except:
        print("No se puede abrir el puerto")

contador = 0
data.write(struct.pack('>B',contador)) 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Sensor1_Title = QtWidgets.QLabel(self.centralwidget)
        self.Sensor1_Title.setGeometry(QtCore.QRect(100, 90, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Sensor1_Title.setFont(font)
        self.Sensor1_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor1_Title.setObjectName("Sensor1_Title")
        self.Sensor2_Title = QtWidgets.QLabel(self.centralwidget)
        self.Sensor2_Title.setGeometry(QtCore.QRect(340, 90, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Sensor2_Title.setFont(font)
        self.Sensor2_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor2_Title.setObjectName("Sensor2_Title")
        self.Sensor3_Title = QtWidgets.QLabel(self.centralwidget)
        self.Sensor3_Title.setGeometry(QtCore.QRect(580, 90, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Sensor3_Title.setFont(font)
        self.Sensor3_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor3_Title.setObjectName("Sensor3_Title")
        self.Button_Plus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Plus.setGeometry(QtCore.QRect(690, 220, 31, 28))
        self.Button_Plus.setObjectName("Button_Plus")
        self.Button_Minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Minus.setGeometry(QtCore.QRect(570, 220, 31, 28))
        self.Button_Minus.setObjectName("Button_Minus")
        self.COM_Title = QtWidgets.QLabel(self.centralwidget)
        self.COM_Title.setGeometry(QtCore.QRect(330, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.COM_Title.setFont(font)
        self.COM_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.COM_Title.setObjectName("COM_Title")
        self.COM_var = QtWidgets.QLabel(self.centralwidget)
        self.COM_var.setGeometry(QtCore.QRect(440, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.COM_var.setFont(font)
        self.COM_var.setObjectName("COM_var")
        self.Sensor1_var = QtWidgets.QLabel(self.centralwidget)
        self.Sensor1_var.setGeometry(QtCore.QRect(94, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.Sensor1_var.setFont(font)
        self.Sensor1_var.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor1_var.setObjectName("Sensor1_var")
        self.Sensor2_var = QtWidgets.QLabel(self.centralwidget)
        self.Sensor2_var.setGeometry(QtCore.QRect(340, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.Sensor2_var.setFont(font)
        self.Sensor2_var.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor2_var.setObjectName("Sensor2_var")
        self.Sensor3_var = QtWidgets.QLabel(self.centralwidget)
        self.Sensor3_var.setGeometry(QtCore.QRect(590, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.Sensor3_var.setFont(font)
        self.Sensor3_var.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor3_var.setObjectName("Sensor3_var")
        self.Dimension1 = QtWidgets.QLabel(self.centralwidget)
        self.Dimension1.setGeometry(QtCore.QRect(200, 160, 16, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.Dimension1.setFont(font)
        self.Dimension1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Dimension1.setObjectName("Dimension1")
        self.Sensor1_var_3 = QtWidgets.QLabel(self.centralwidget)
        self.Sensor1_var_3.setGeometry(QtCore.QRect(440, 160, 16, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.Sensor1_var_3.setFont(font)
        self.Sensor1_var_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Sensor1_var_3.setObjectName("Sensor1_var_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        def suma ():
            global contador
            contador = contador + 1
            if contador > 255:
                contador = 0
            data.write(struct.pack('>B',contador))
            self.Sensor3_var.setText(str(contador))
            

        def resta ():
            global contador
            contador = contador - 1
            if contador < 0:
                contador = 255
            data.write(struct.pack('>B',contador))
            self.Sensor3_var.setText(str(contador))

        s1 = str(ord(data.read())) + "." + str(ord(data.read()))
        s2 = str(ord(data.read())) + "." + str(ord(data.read()))
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Port"))
        self.Sensor1_Title.setText(_translate("MainWindow", "Sensor 1"))
        self.Sensor2_Title.setText(_translate("MainWindow", "Sensor 2"))
        self.Sensor3_Title.setText(_translate("MainWindow", "Sensor 3"))
        self.Button_Plus.setText(_translate("MainWindow", "+"))
        self.Button_Minus.setText(_translate("MainWindow", "-"))
        self.COM_Title.setText(_translate("MainWindow", "COM:"))
        self.COM_var.setText(_translate("MainWindow", numero))
        self.Sensor1_var.setText(_translate("MainWindow", s1))
        self.Sensor2_var.setText(_translate("MainWindow", s2))
        self.Sensor3_var.setText(_translate("MainWindow", str(contador)))
        self.Dimension1.setText(_translate("MainWindow", "V"))
        self.Sensor1_var_3.setText(_translate("MainWindow", "V"))
        self.Button_Plus.clicked.connect(suma)
        self.Button_Minus.clicked.connect(resta)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

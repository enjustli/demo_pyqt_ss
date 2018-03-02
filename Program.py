



import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import *
#Enable High DPI display with PyQt5
if hasattr(PyQt5.QtCore.Qt,'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling,True)
if hasattr(PyQt5.QtCore.Qt,'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(PyQt5.QtCore.Qt.AA_UseHighDpiPixmaps,True)



from shadowsocks_pyqt5 import (Ui_Form)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui=Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())




"""
#high level support for doing this and that.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
APP = QApplication(sys.argv)
WINDOW = QWidget()
WINDOW.setGeometry(50, 50, 500, 300)
WINDOW.setWindowTitle('Hello, world')
WINDOW.show()
sys.exit(APP.exec_())

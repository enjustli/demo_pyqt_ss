# 用户界面逻辑控制模块


from ui.shadowsocks_pyqt5 import (Ui_Form)
from PyQt5.QtWidgets import *
from PyQt5 import *


#远程服务器登录信息
class server_info_struct(object):
    def __init__(self):
        self.server_ip = "127.0.0.1"
        self.port = "8088"
        self.password = "password"
        self.encryption = "rc4-md5"
        self.timeout = "300"  #ms
        pass

    pass


#代理设置结构
class proxy_settings(object):
    def __init__(self):
        self.proxyport = "1080"
        self.enablesystemagent = "True"
        self.actingalltraffic = "False"
        self.httpproxy = "127.0.0.1:2598"
        self.socksproxy = "127.0.0.1:2589"
        pass

    pass


#逻辑控制，用户交互
class ssui(Ui_Form):
    def __init__(self, Form):
        #---
        self.form = Form
        self.current_server_id = -1
        self.serverlist = []
        self.proxysetings = proxy_settings()
        #---
        self.setupUi(Form)
        #---设定信号和槽
        self.button_add.clicked.connect(self.add_server)
        self.button_delete.clicked.connect(self.delete_server)
        self.button_copy.clicked.connect(self.copy_server)
        self.button_ok.clicked.connect(self.click_ok)
        self.button_cancel.clicked.connect(self.click_cancel)
        self.checkBox_show_password.clicked.connect(self.setpassword_show)
        pass

    def generate_server_info(self):
        sinf = server_info_struct()
        sinf.server_ip = self.lineEdit_serverip.text()
        sinf.port = self.lineEdit_server_port.text()
        sinf.password = self.lineEdit_password.text()
        sinf.encryption = self.comboBox_encryption.currentText()
        sinf.timeout = self.lineEdit_timeout.text()
        return sinf
        pass

    def generate_proxy_setting(self):
        proset = proxy_settings()
        proset.proxyport=self.lineEdit_Proxy_port.text()
        proset.enablesystemagent = self.checkBox_enable_system_agent.isChecked()
        proset.actingalltraffic = self.checkBox_acting_all_traffic.isChecked()
        proset.httpproxy = self.textEdit_httpproxy.toPlainText()
        proset.socksproxy = self.textEdit_socksproxy.toPlainText()
        return proset
        pass

    def add_server(self):

        pass

    def delete_server(self):
        pass

    def copy_server(self):
        pass

    def click_ok(self):
        pass

    def click_cancel(self):
        pass

    def setpassword_show(self):
        if self.checkBox_show_password.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)
        pass

    #---选择服务器
    def select_server_inf(self):
        pass

    pass
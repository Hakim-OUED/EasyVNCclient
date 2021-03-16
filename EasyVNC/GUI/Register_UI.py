# -*- coding: utf-8 -*-
import os

from PyQt5 import QtCore, QtWidgets

from EasyVNC.localData.utils import *
import EasyVNC.GUI.icons_rc  # pylint: disable=unused-import
from EasyVNC.GUI.customized import PasswordEdit

import socket
import ssl

class RegisterForm(QtWidgets.QWidget):
    """Basic login form.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("REGISTER EasyVPN")
        self.setup_ui()

    def setup_ui(self):
        """Setup the login form.
        """
        self.resize(480, 825)
        # remove the title bar
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet(
            """
            QPushButton {
                border-style: outset;
                border-radius: 0px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #cf7500;
                border-style: inset;
            }
            QPushButton:pressed {
                background-color: #ffa126;
                border-style: inset;
            }
            """
        )


        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.widget = QtWidgets.QWidget(self)
        self.widget.setMaximumSize(QtCore.QSize(800, 800))
        self.widget.setStyleSheet(".QWidget{background-color: rgb(20, 20, 40);}")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)

        self.lbl_title = QtWidgets.QLabel(self.widget)
        self.lbl_title.setMinimumSize(QtCore.QSize(100, 150))
        self.lbl_title.setMaximumSize(QtCore.QSize(150, 150))
        self.lbl_title.setStyleSheet("image: url(:/icons/icons/rocket_48x48.png);")
        self.lbl_title.setStyleSheet("color: rgb(231, 231, 231);\n"
                                      "font: 17pt \"Verdana\";\n"
                                      "border: 2px solid orange;\n"
                                      "padding: 5px;\n"
                                      "border-radius: 3px;\n"
                                      "opacity: 200;\n"
                                      "")
        self.verticalLayout_3.addWidget(self.lbl_title, 0, QtCore.Qt.AlignHCenter)

        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(50, 75, 59, -1)
        self.lbl_msg = QtWidgets.QLabel(self.widget)
        self.lbl_msg.setGeometry(QtCore.QRect(70, 180, 351, 31))
        self.lbl_msg.setObjectName("label")
        self.lbl_msg.setHidden(True)
        self.lbl_msg.setStyleSheet(
            "QLabel"
            "{"
                "text-align: left;"
                "font-weight: bold;"
                "color : rgb(255, 0, 0);"
                "font-size: 15px;"
                "height: 1em;"
                "width: 2ch;"
                "font-family: Arial"
                "}")
        self.lbl_username = QtWidgets.QLabel(self.widget)
        self.lbl_username.setStyleSheet("color: rgb(231, 231, 231);\n"
                                   "font: 15pt \"Verdana\";")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_username)

        self.edt_username = QtWidgets.QLineEdit(self.widget)
        self.edt_username.setMinimumSize(QtCore.QSize(0, 40))
        self.edt_username.setStyleSheet("QLineEdit {\n"
                                    "color: rgb(231, 231, 231);\n"
                                    "font: 15pt \"Verdana\";\n"
                                    "border: None;\n"
                                    "border-bottom-color: white;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 0 8px;\n"
                                    "background: rgb(20, 20, 40);\n"
                                    "selection-background-color: darkgray;\n"
                                    "}")
        self.edt_username.setPlaceholderText("Username")
        self.edt_username.setFocus(True)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edt_username)


        self.lbl_mail = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_mail)

        self.edt_mail = QtWidgets.QLineEdit(self.widget)
        self.edt_mail.setMinimumSize(QtCore.QSize(0, 40))
        self.edt_mail.setStyleSheet("QLineEdit {\n"
                                      "color: rgb(231, 231, 231);\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "border: None;\n"
                                      "border-bottom-color: white;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(20, 20, 40);\n"
                                      "selection-background-color: darkgray;\n"
                                      "}")
        self.edt_mail.setPlaceholderText("aaaaa@domain.xx")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edt_mail)

        self.lbl_mdp1 = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_mdp1)

        self.edt_mdp1 = PasswordEdit(self.widget)
        self.edt_mdp1.setMinimumSize(QtCore.QSize(0, 40))
        self.edt_mdp1.setStyleSheet("QLineEdit {\n"
                                      "color: orange;\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "border: None;\n"
                                      "border-bottom-color: white;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(20, 20, 40);\n"
                                      "selection-background-color: darkgray;\n"
                                      "}")
        self.edt_mdp1.setPlaceholderText("Password")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.edt_mdp1)
        self.edt_mdp1.setEchoMode(QtWidgets.QLineEdit.Password)


        self.lbl_mdp2 = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_mdp2)

        self.edt_mdp2 = PasswordEdit(self.widget)
        self.edt_mdp2.setMinimumSize(QtCore.QSize(0, 40))
        self.edt_mdp2.setStyleSheet("QLineEdit {\n"
                                      "color: orange;\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "border: None;\n"
                                      "border-bottom-color: white;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(20, 20, 40);\n"
                                      "selection-background-color: darkgray;\n"
                                      "}")
        self.edt_mdp2.setPlaceholderText("Confirm Password")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.edt_mdp2)
        self.edt_mdp2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("border: 2px solid white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)

        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setStyleSheet("border: 2px solid white;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_3)

        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setStyleSheet("border: 2px solid orange;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_2)

        self.btn_signIn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_signIn.sizePolicy().hasHeightForWidth())

        self.btn_signIn.setSizePolicy(sizePolicy)
        self.btn_signIn.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_signIn.setAutoFillBackground(False)
        self.btn_signIn.setStyleSheet("color: rgb(231, 231, 231);\n"
                                      "font: 17pt \"Verdana\";\n"
                                      "border: 2px solid orange;\n"
                                      "padding: 5px;\n"
                                      "border-radius: 3px;\n"
                                      "opacity: 200;\n"
                                      "")
        self.btn_signIn.setAutoDefault(True)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.btn_signIn)

        self.btn_register = QtWidgets.QPushButton(self.widget)
        self.btn_register.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_register.setStyleSheet("color: rgb(231, 231, 231);\n"
                                        "font: 17pt \"Verdana\";\n"
                                        "border: 2px solid orange;\n"
                                        "padding: 5px;\n"
                                        "border-radius: 3px;\n"
                                        "opacity: 200;\n"
                                        "")
        self.btn_register.setDefault(False)
        self.btn_register.setFlat(False)
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.btn_register)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.verticalLayout_3.addLayout(self.formLayout_2)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_signIn.clicked.connect(self.signIn)
        self.btn_register.clicked.connect(self.register)



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.lbl_msg.setText(_translate("Login",
                                      "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">" +
                                      "Les données saisies ne respectent les formats correctes " + "</span></p></body></html>"))
        self.lbl_title.setText(_translate("Form", "Register"))

        self.lbl_username.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/user_32x32.png\"/></p></body></html>"))
        self.lbl_mail.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/mail_32x32.png\"/></p></body></html>"))
        self.lbl_mdp1.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/lock_or_32x32.png\"/></p></body></html>"))
        self.lbl_mdp2.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/lock_or_32x32.png\"/></p></body></html>"))
        self.btn_signIn.setText(_translate("Form", "Sign In"))
        self.btn_register.setText(_translate("Form", "Register"))

    def register(self):
        self.username = self.edt_username.text()
        self.usermail = self.edt_mail.text()
        self.password1 = self.edt_mdp1.text()
        self.password2 = self.edt_mdp2.text()
        valid_data = self.input_validator(self.username, self.usermail, self.password1, self.password2)
        if valid_data:
            self.insert_data()

    def signIn(self):
        self.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = GUI.Login_UI.LoginForm()
        self.ui.show()

    def insert_data(self):
        self.socket_data = read_socket_data()
        hostname = self.socket_data['hostname']
        port = int(self.socket_data['socket_port'])
        context = ssl.create_default_context()
        cert = os.path.dirname(os.path.realpath(__file__)) + '/../Cert/cert.pem'
        context.load_verify_locations(cert)
        conn = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_side=False,
                                   server_hostname=hostname)
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((hostname, port))
        response = conn.recv(2048)

        req = 2098

        data = str(req) + ";" + self.username + ";" + self.usermail + ";" + self.password1
        conn.send(str.encode(data))

        cle = conn.recv(1024)
        end = b"SUCCESSFULL REGISTERED! You can SignIn"

        if not cle.isalpha():
            f = open("./client.conf", 'wb')  # Open in binary

            while (cle):
                f.write(cle)
                print("reception des données")
                if cle == end:
                    break
                cle = conn.recv(1024)
            f.close()
            response = "SUCCESSFULL REGISTERED! You can SignIn"

        # Receive response
        #response = conn.recv(2048)
        #response = response.decode()
        if "successfull registered" in response.lower():
            self.lbl_msg.setText(response)
            self.lbl_msg.setStyleSheet("color: rgb(0, 230, 0);")
            self.lbl_msg.setHidden(False)
        else:
            self.lbl_msg.setText(response)
            self.lbl_msg.setStyleSheet("color: rgb(255, 0, 0);")
            self.lbl_msg.setHidden(False)

        print(response)
        conn.close()


    def input_validator(self, username, usermail, password1, password2):
        import re
        regex_name = "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"
        match_name = re.match(regex_name, username)
        regex_mail = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        match_mail = re.match(regex_mail, usermail)
        if match_name == None:
            print("Erreur de saisie du username")
            self.lbl_msg.setText("Erreur de saisie du username! Verifier le format!")
            self.lbl_msg.setHidden(False)
            return False
        elif match_mail == None:
            print("Erreur de saisie de l'addresse mail")
            self.lbl_msg.setHidden(False)
            return False
        elif password1 != password2:
            print("Erreur de mot de passe")
            self.lbl_msg.setHidden(False)
            return False
        elif password1 == "" and password2 == "":
            print("Erreur de mot de passe vide")
            self.lbl_msg.setHidden(False)
            return False
        elif len(password1) < 8:
            print("Erreur de mot de passe trop court")
            self.lbl_msg.setHidden(False)
            return False
        return True
""""

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_form = RegisterForm()
    login_form.show()
    sys.exit(app.exec_()) """
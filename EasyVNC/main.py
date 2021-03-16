import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.Login_UI import LoginForm


app = QApplication(sys.argv)
login_form = LoginForm()
login_form.show()

sys.exit(app.exec_())

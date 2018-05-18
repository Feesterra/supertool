import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import supertool
import supertool.weather_main
import supertool.weather_second
import supertool.weather


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        """Constructor for GUI eather forecast second window."""

        super(Dialog, self).__init__()

        self.ui = supertool.weather_second.Ui_Dialog()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        """Defines actions when dialog window is closed."""

        self.ui.textEdit.clear()
        supertool.work.hashes.clear()
        self.close()


class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        """Constructor for GUI weather forecast main window."""

        super(MainApplication, self).__init__()

        self.secondWin = None

        self.ui = supertool.weather_main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.button_pressed)

    def button_pressed(self):
        """Actions when button 'Search' is pressed."""

        location = self.ui.lineEdit.text()
        self.openWin()
        days = int(self.ui.spinBox.text())

        if location and location.isalpha():
            self.secondWin.ui.textEdit.append(
                supertool.weather.nominatim_weather_daily(location, token_id='1b0ca47d89658cde3cc64234f71e0fc7',
                                                          cnt=days))
        else:
            self.secondWin.ui.textEdit.append("Enter (correct) location.")

    def openWin(self):
        """Opens the second window with results."""

        if not self.secondWin:
            self.secondWin = Dialog()
        self.secondWin.show()

    def closeEvent(self, QCloseEvent):
        """Defines actions when main window is closed."""

        self.close()


app = QtWidgets.QApplication(sys.argv)

window = MainApplication()
window.show()

sys.exit(app.exec_())
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import supertool
import supertool.similar_start
import supertool.dialog
import supertool.work


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        """Constructor for GUI similar_files second window."""

        super(Dialog, self).__init__()

        self.ui = supertool.dialog.Ui_Dialog()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        """Defines actions when dialog window is closed."""

        self.ui.textEdit.clear()
        supertool.work.hashes.clear()
        self.close()


class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        """Constructor for GUI similar_files main form."""

        super(MainApplication, self).__init__()

        self.secondWin = None

        self.ui = supertool.similar_start.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.button_pressed)

    def button_pressed(self):
        """Actions when button 'Search' is pressed."""

        directory = self.ui.lineEdit.text()
        self.openWin()

        if directory:
            self.secondWin.ui.textEdit.append(supertool.work.find_duplicates(directory))
        else:
            self.secondWin.ui.textEdit.append("Enter a directory.")

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

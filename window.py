"""
Very simple calculator
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import buttons
import sys
import functools


class MainApplication(QtWidgets.QMainWindow):
    """Descripts calculator form and realisation"""

    def __init__(self):
        """Constructor for GUI calculator form"""

        super(MainApplication, self).__init__()
        self._x = 1

        self.num1 = None
        self.num2 = None
        self.oper = None
        self.minus_num = False

        self.ui = buttons.Ui_MainWindow()
        self.ui.setupUi(self)

        for i in range(9):
            col = i % 3
            row = i // 3

            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(30)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName("button_{}".format(i))
            self.ui.gridLayout.addWidget(button, row, col, 1, 1)
            button.setText(str(i + 1))

            button.clicked.connect(functools.partial(self.button_pressed, i+1))
        self.ui.Zero.clicked.connect(functools.partial(self.button_pressed, 0))
        self.ui.exp.clicked.connect(self.exponenta)

        self.ui.buttonA1.clicked.connect(self.addition)
        self.ui.buttonA2.clicked.connect(self.substraction)
        self.ui.buttonA3.clicked.connect(self.multiplication)
        self.ui.buttonA4.clicked.connect(self.division)
        self.ui.buttonA5.clicked.connect(self.itog)
        self.ui.buttonA6.clicked.connect(self.deleting)

    def button_pressed(self, number):
        """Determines action for buttons with numbers 1-9. Sets num1 and num2 for future operations.

        :param number: number on button pressed
        :return: None. Displays on LCD Number field
        """

        if self.num1 is None:

            self.num1 = number
            self.ui.lcdNumber.display(number)
        else:
            if self.oper is None:
                self.num1 = str(self.num1) + str(number)
                self.ui.lcdNumber.display(self.num1)
            else:
                if self.num2 is None:
                    self.num2 = number
                elif self.num2 is not None:
                    self.num2 = str(self.num2) + str(number)
                self.ui.lcdNumber.display(self.num2)

    def addition(self):
        """Determins behavior when button '+' is pressed.
        Changes self.oper variable and displays '' to the LCD display.
        """

        if self.oper is not None:
            self.itog()
        self.oper = '+'
        self.ui.lcdNumber.display('')

    def substraction(self):
        """Determins behavior when button '-' is pressed.
        Changes self.oper variable and displays '' to the LCD display.
        """

        if self.oper is not None:
            self.itog()
        self.oper = '-'
        self.ui.lcdNumber.display('')

    def multiplication(self):
        """Determins behavior when button '*' is pressed.
        Changes self.oper variable and displays '' to the LCD display.
        """

        if self.oper is not None:
            self.itog()
        self.oper = '*'
        self.ui.lcdNumber.display('')

    def division(self):
        """Determins behavior when button '/' is pressed.
        Changes self.oper variable and displays '' to the LCD display.
        """

        if self.oper is not None:
            self.itog()
            print(self.num1, self.num2)
        self.oper = '/'
        self.ui.lcdNumber.display('')

    def exponenta(self):
        """Determins behavior when button 'exp' is pressed.
        Changes self.oper variable and displays '' to the LCD display.
        """

        self.oper = 'exp'
        self.ui.lcdNumber.display('')

    def deleting(self):
        """Chsanges self.num1, self.num2, self.oper to None. Displays '' on LCD."""

        self.num1 = None
        self.num2 = None
        self.oper = None
        self.ui.lcdNumber.display(0)

    def itog(self):
        """Determins behavior when button '=' is pressed.
        Changes self.num1, self.num2, self.oper variables and displays result(n) to the LCD display.
        If pressing logic is incorrect, displays 'Error' on LCD.
        """

        if self.num2 is None or self.num1 is None:
            self.ui.lcdNumber.display('Error')
        else:

            self.num1 = int(self.num1)
            self.num2 = int(self.num2)

            if self.oper == '+':
                n = self.num1 + self.num2
            elif self.oper == '-':
                n = self.num1 - self.num2
            elif self.oper == '*':
                n = self.num1 * self.num2
            elif self.oper == '/':
                n = self.num1 / self.num2
            elif self.oper == 'exp':
                n = self.num1 ** self.num2
            self.ui.lcdNumber.display(n)
            self.num1 = n
            self.num2 = None
            self.oper = None


app = QtWidgets.QApplication(sys.argv)
window = MainApplication()
window.show()
sys.exit(app.exec_())


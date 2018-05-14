"""
True calculator.
"""
import functools
from operator import add, sub, truediv, pow, mul

from PyQt5 import QtCore, QtGui, QtWidgets

import supertool.calc_gui.buttons as buttons


class MainApplication(QtWidgets.QMainWindow):
    """
    Class that presents logic of the true calc_gui.
    """

    def __init__(self):
        """
        Initialize application.
        """
        super(MainApplication, self).__init__()
        self.ui = buttons.Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_operation = False
        self.numberone = ''
        self.numberdva = ''
        self.result = None
        self.operation = ''

        for i in range(10):
            if i == 0:
                col, row = 1, 3
            else:
                col, row = (i - 1) % 3, (i - 1) // 3
            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                               QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName(f'button_{i}')
            self.ui.gridLayout.addWidget(button, row, col, 1, 1)
            button.setText(str(i))
            button.clicked.connect(functools.partial(self.button_preassed, i))

        self.ui.plus.clicked.connect(self.plus_pressed)
        self.ui.division.clicked.connect(self.div_pressed)
        self.ui.power.clicked.connect(self.power_pressed)
        self.ui.sub.clicked.connect(self.sub_pressed)
        self.ui.multypli.clicked.connect(self.mul_pressed)
        self.ui.reset.clicked.connect(self.reset)
        self.ui.result.clicked.connect(self.enter_pressed)
        self.ui.lcd.display('')

    def button_preassed(self, number):
        """
        Function to handle digit button pressure.

        :param number: digit for a corresponding button.
        :type number: int.
        :return: None.
        """
        if self.is_operation and self.numberone != '' or\
                                self.result != None and self.numberone != '':
            self.numberdva += str(number)
            self.ui.lcd.display(float(self.numberdva))
        else:
            self.numberone += str(number)
            self.ui.lcd.display(float(self.numberone))
            self.result = None


    def plus_pressed(self):
        """
        Function to handle addition operation.

        :return: None.
        """
        self.calculation()
        self.operation = '+'

    def sub_pressed(self):
        """
        Function to handle subtraction operation.

        :return: None.
        """
        self.calculation()
        self.operation = '-'

    def mul_pressed(self):
        """
        Function to handle multiply operation.

        :return: None.
        """
        self.calculation()
        self.operation = '*'


    def power_pressed(self):
        """
        Function to handle raise to a power operation.

        :return: None.
        """
        self.calculation()
        self.operation = '^'

    def div_pressed(self):
        """
        Function to handle division operation.

        :return: None.
        """
        self.calculation()
        self.operation = '/'

    def calculation(self):
        """
        Function that represents logic of calculation.

        :return:None.
        """
        err = 0
        if self.numberone != '':
            self.is_operation = True
        if self.result != None:
            self.numberone = str(self.result)
        if self.numberone != '' and self.numberdva != '':
            num1 = float(self.numberone)
            num2 = float(self.numberdva)
            if self.operation == '+':
                self.result = add(num1, num2)
            elif self.operation == '-':
                self.result = sub(num1, num2)
            elif self.operation == '*':
                self.result = mul(num1, num2)
            elif self.operation == '/':
                try:
                    self.result = truediv(num1, num2)
                except ZeroDivisionError:
                    self.reset()
                    err = 1
            elif self.operation == '^':
                self.result = pow(num1, num2)
            if err == 0:
                self.ui.lcd.display(self.result)
                self.numberdva = ''

    def enter_pressed(self):
        """
        Function to handle result button '='.

        :return: None.
        """
        self.calculation()
        self.operation = ''
        if self.numberdva == '' and self.numberone == '':
            self.ui.lcd.display('')
        elif self.result == None:
            self.result = float(self.numberone)
            self.ui.lcd.display(self.result)
        self.numberone = ''
        self.is_operation = False

    def reset(self):
        """
        Function to reset all attributes.

        :returns: None.
        """
        self.ui.lcd.display('')
        self.is_operation = False
        self.numberdva = ''
        self.numberone = ''
        self.result = None

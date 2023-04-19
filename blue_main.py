'''Конвертер валют'''
import sys
from currency_converter import CurrencyConverter
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui_cal import Ui_MainWindow


class CurrencyConv(QMainWindow):
    '''на основе класса создание функции'''
    def __init__(self):
        super().__init__()
        #super(CurrencyConv, self).__init__()
        self.ui_cal = Ui_MainWindow()
        self.ui_cal.setupUi(self)
        self.init_UI()


    def init_UI(self):
        '''на основе класса создание функции'''
        self.setWindowTitle("Конвертер валют")
        self.setWindowIcon(QIcon('exchanging.png'))

        self.ui_cal.input_amount.setPlaceholderText("У меня есть:")
        self.ui_cal.from_currency.setPlaceholderText("Из валюты:")
        self.ui_cal.to_currency.setPlaceholderText("В валюту:")
        self.ui_cal.output_amount.setPlaceholderText("Я получу:")
        self.ui_cal.pushButton.clicked.connect(self.converter)

    def converter(self):
        '''на основе класса создание функции'''
        currency = CurrencyConverter()
        from_currency = self.ui_cal.from_currency.text()
        to_currency = self.ui_cal.to_currency.text()
        input_amount = int(self.ui_cal.input_amount.text())

        output_amount = round(currency.convert(input_amount,from_currency, to_currency), 2)
        self.ui_cal.output_amount.setText(str(output_amount))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = CurrencyConv()
    application.show()
    sys.exit(app.exec())

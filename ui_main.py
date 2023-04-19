
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
#from forex_python.converter import CurrencyRates
from currency_converter import CurrencyConverter
from datetime import date

class CurrencyConv(QMainWindow):
    def __init__(self):
        super().__init__()
        #super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.setWindowTitle("Конвертер валют")
        self.setWindowIcon(QIcon('exchanging.png'))

        self.ui.input_currency.setPlaceholderText("Из валюты:")
        self.ui.input_amount.setPlaceholderText("У меня есть:")
        self.ui.output_currency.setPlaceholderText("В валюту:")
        self.ui.output_amount.setPlaceholderText("Я получу:")
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        #c = CurrencyConverter()
        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())
        #output_amount = f'{c.convert(input_amount, input_currency, input_currency)}'
        #output_amount = c.convert(input_amount, str(input_currency), str(input_currency))
        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2) # '%s' % (date.today())), 2)
        self.ui.output_amount.setText(str(output_amount))




if __name__ == '__main__':
    app = QApplication(sys.argv)

    application = CurrencyConv()
    application.show()
    sys.exit(app.exec())


    #MainWindow = QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())



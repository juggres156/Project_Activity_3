import PyQt5
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton,QMainWindow,QDesktopWidget, QRadioButton, QVBoxLayout, QHBoxLayout
import sys
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ"

class Travel(QWidget):
    def __init__(self):
        super().__init__()
        
        self.width = 1400
        self.height = 900
        self.setWindowTitle("MapQuest")
        self.setFixedSize(self.width,self.height)

        self.Center() #put the window on the center of the screen
        self.CityChoices()
        self.Destination()
        self.show()


    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def CityChoices(self):
        vbox_layout = QVBoxLayout()
        self.washington_btn = QRadioButton("Washington",self)
        vbox_layout.addWidget(self.washington_btn)
        self.setLayout(vbox_layout)

    def Destination(self):
        hbox_dest = QHBoxLayout()
        self.baltimore_btn = QRadioButton("Baltimore",self)
        self.baltimore_btn.move(100,100)
        hbox_dest.addWidget(self.baltimore_btn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Travel()
    print("Running....")
    sys.exit(app.exec_())

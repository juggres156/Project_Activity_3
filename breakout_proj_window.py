import PyQt5
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton,QMainWindow,QDesktopWidget
import sys

class Travel(QWidget):
    def __init__(self):
        super().__init__()
        
        self.width = 700
        self.height = 500

        self.Center() #put the window on the center of the screen
        self.show()

    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Travel()
    print("Running....")
    sys.exit(app.exec_())

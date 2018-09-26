import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import jclftp
from openpyxl import load_workbook
import time

class Example(QWidget):
    # initialize here
    def __init__(self):
        super().__init__()        
        self.loading()
    # loading image                
    def loading(self):
        splash_pix = QPixmap('img/bee.jpg')
        splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
        splash.show()
        time.sleep(1)    
        self.initUI()

    def initUI(self):           	        
        self.setGeometry(300, 300, 250, 150)        	
        self.setWindowTitle('Message box')    
        self.label = QLabel('Dit is het control center van Andre Jochemsen',self)
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)    
    ex = Example()
    sys.exit(app.exec_())
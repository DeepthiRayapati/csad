import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication,QSplashScreen,QLabel,QPushButton
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
        splash_pix = QPixmap('img/Koala.jpg')
        splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
        splash.show()
        time.sleep(1)    
        self.initUI()

    def initUI(self):           	        
        self.setGeometry(300, 300, 250, 150)    
        self.button = QPushButton('Uttam', self)  
        self.button.setToolTip('This is an example button') 
        self.button.clicked.connect(self.on_click) 	
        self.setWindowTitle('Message box')    
        #self.label = QLabel('Hi dis is Deepthi',self)
        self.show()

    def on_click(self):
        print("Button Clicked!")           	        
  
        
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
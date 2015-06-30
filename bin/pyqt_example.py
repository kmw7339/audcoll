#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class EcaRecGui(QtGui.QWidget):
    
    def __init__(self):
        super(EcaRecGui, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        qbtn = QtGui.QPushButton('Start Recording', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(250, 50)       
        


        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('EcaColl')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = EcaRecGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

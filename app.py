from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                        QHBoxLayout, QVBoxLayout, QBoxLayout, QMainWindow, QFrame, QMenu, QTabWidget, QComboBox, QGridLayout, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt, QSize, QPointF, QRect, QMargins, QAbstractTableModel
from PyQt5.QtGui import QLinearGradient, QPalette, QColor, QIcon, QPixmap, QFont 
from styles.style import *
from Examples.rungeKutta import RK1, RK2, RK3, RK4, model, sqrt
import sys

""" App Objets - App Widgets """

class SecondTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        # layout para el objeto SecondTabWidget.
        self.layout = QVBoxLayout(self)

        # Instacia QtabWidget.
        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        self.tabs.setFixedWidth(1000)
        
        # pestaña 1
        self.tab1 = QFrame(self)    # Primera pestaña, se pasa como widget.
        self.tab1.setAutoFillBackground(True)
        self.tab1.setStyleSheet("""
                                    background-color: white;
                                    
                                """) 

        # pestaña 2
        self.tab2 = QFrame(self)    
        self.tab2.setAutoFillBackground(True)
        self.tab2.setStyleSheet("""
                                    background-color: white;
                                    
                                """) 

        # Pestaña 3
        self.tab3 = QFrame(self)    
        self.tab3.setAutoFillBackground(True)
        self.tab3.setStyleSheet("""
                                    background-color: white;
                                    
                                """) 

        # Pestaña 4
        self.tab4 = QFrame(self)    
        self.tab4.setAutoFillBackground(True)
        self.tab4.setStyleSheet("""
                                    background-color: white;
                                    
                                """)
        
        # Add new tabs in QtabWidget.
        self.tabs.addTab(self.tab1, "RK1")
        self.tabs.addTab(self.tab2, "RK2")
        self.tabs.addTab(self.tab3, "RK3")
        self.tabs.addTab(self.tab4, "RK4")  # Añadimos pestañas a tabs.

        # añadimos el widget en layout de SecondTabWidget.
        self.layout.addWidget(self.tabs)

        # definimos el layout.
        self.setLayout(self.layout)

class FirstTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        self.tabs.setFixedWidth(200)
        
        self.tab1 = QWidget()    # Primera pestaña, se pasa como widget.
        self.tab1.setObjectName("tab1_firts")
        self.tab1.setStyleSheet("background-color: white;")

        self.tabs.addTab(self.tab1, "User Values")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def menuHand(self):
        print("pepe")

""" App Widnows """
class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        """ Propieties AppMain """
        self.widget_db = QWidget()          # widget for storage grid layout.
        self.grid_layout = QGridLayout()    # grid layout for data base registers.
        self.rows = None        # rows in grid layout.
        self.Columns = None     # columns in grid layout.
        self.w = 1330           # width window.
        self.h = 480            # height window.
        
        """ Configuration AppMain"""
        self.setWindowTitle("Runge Kutta Panel - 23ft")
        self.setFixedSize(self.w, self.h)   # config initial size.
        self.setStyleSheet(main_css)        # define style sheet 
        
        """ Constants Tables"""
        self.table_enable = False
        self.table_rk1 = None
        self.table_rk2 = None
        self.table_rk3 = None
        self.table_rk4 = None
        
        self.layout_table_rk1 = None
        self.layout_table_rk2 = None
        self.layout_table_rk3 = None
        self.layout_table_rk4 = None
        
        self.equation = None
        self.Xo = None
        self.Xf = None
        self.Yo = None
        self.n = None
        self.realdata = None
        self.step = None
        self.constant = None 
        
        """ Build Widget """
        self.initUi()

    def initUi(self):

        """
            <MainDiv>
            Principal Div Block in AppMain
        """
        self.frame = QFrame(self)               #frame Main.
        self.frame.setObjectName("AppMainFrame")
        #self.frame.setFrameShape(QFrame.NoFrame)
        #self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setAutoFillBackground(True)
        self.frame.setFixedWidth(self.w)
        self.frame.setFixedHeight(self.h)

        
        self.mainbox = QHBoxLayout(self.frame)  # layout, first block of tabs and second block of tabs.
        self.first = FirstTabWidget()           # first block of tabs
        self.second = SecondTabWidget()         # second block of tabs
        
              
        """ 
            <FirstTabWidget>
            Actions Data Base 
        """
        self.layout_tools = QVBoxLayout(self.first.tab1)
        self.layout_tools.setContentsMargins(0,0,0,0)   # quitar magins del layout.
        
        
        self.first_frame = QFrame()
        self.second_frame = QFrame()
        self.second_frame.setObjectName("pepe")
        self.second_frame.setFixedWidth(300)
        self.second_frame.setFrameShape(QFrame.NoFrame)
        self.second_frame.setFrameShadow(QFrame.Sunken)
        self.second_frame.setAutoFillBackground(True)
        
        self.label_equ = QLabel("y'", self.first_frame)
        self.label_equ.setStyleSheet(label_user)
        self.label_equ.move(10,  50)
        self.entry_equ = QLineEdit(self.first_frame)
        self.entry_equ.setStyleSheet(entrys)
        self.entry_equ.setFixedWidth(120)
        self.entry_equ.setPlaceholderText("Equation")
        self.entry_equ.setClearButtonEnabled(True)
        self.entry_equ.move(50,55)
        self.entry_equ.setText("x*(10-y(x))")
        
        self.label_xo = QLabel("Xo", self.first_frame)
        self.label_xo.setStyleSheet(label_user)
        self.label_xo.move(10,  50+40)
        self.entry_xo = QLineEdit(self.first_frame)
        self.entry_xo.setStyleSheet(entrys)
        self.entry_xo.setFixedWidth(120)
        self.entry_xo.setPlaceholderText("Xo")
        self.entry_xo.setClearButtonEnabled(True)
        self.entry_xo.move(50,55+40)
        self.entry_xo.returnPressed.connect(self.upload)
        
        self.label_xf = QLabel("Xf", self.first_frame)
        self.label_xf.setStyleSheet(label_user)
        self.label_xf.move(10,  50+40+40)
        self.entry_xf = QLineEdit(self.first_frame)
        self.entry_xf.setStyleSheet(entrys)
        self.entry_xf.setFixedWidth(120)
        self.entry_xf.setPlaceholderText("Xf")
        self.entry_xf.setClearButtonEnabled(True)
        self.entry_xf.move(50,55+40+40)
        self.entry_xf.returnPressed.connect(self.upload)
        
        
        self.label_yo = QLabel("Yo", self.first_frame)
        self.label_yo.setStyleSheet(label_user)
        self.label_yo.move(10,  50+40+40+40)
        self.entry_yo = QLineEdit(self.first_frame)
        self.entry_yo.setStyleSheet(entrys)
        self.entry_yo.setFixedWidth(120)
        self.entry_yo.setPlaceholderText("Yo")
        self.entry_yo.setClearButtonEnabled(True)
        self.entry_yo.move(50,55+40+40+40)
        self.entry_yo.returnPressed.connect(self.upload)
        
        self.label_n = QLabel("n", self.first_frame)
        self.label_n.setStyleSheet(label_user)
        self.label_n.move(10,  50+40+40+40+40)
        self.entry_n = QLineEdit(self.first_frame)
        self.entry_n.setStyleSheet(entrys)
        self.entry_n.setFixedWidth(120)
        self.entry_n.setPlaceholderText("n")
        self.entry_n.setClearButtonEnabled(True)
        self.entry_n.move(50,55+40+40+40+40)
        self.entry_n.returnPressed.connect(self.upload)

        self.label_h = QLabel("h", self.first_frame)
        self.label_h.setStyleSheet(label_user)
        self.label_h.move(10,  50+40+40+40+40+40)
        self.entry_h = QLineEdit(self.first_frame)
        self.entry_h.setStyleSheet(entrys)
        self.entry_h.setFixedWidth(120)
        self.entry_h.setPlaceholderText("h")
        self.entry_h.setClearButtonEnabled(True)
        self.entry_h.move(50,55+40+40+40+40+40)
        self.entry_h.returnPressed.connect(self.upload)

        self.label_c1 = QLabel("C1", self.first_frame)
        self.label_c1.setStyleSheet(label_user)
        self.label_c1.move(10,  50+40+40+40+40+40+40)
        self.entry_c1 = QLineEdit(self.first_frame)
        self.entry_c1.setStyleSheet(entrys)
        self.entry_c1.setFixedWidth(120)
        self.entry_c1.setPlaceholderText("C1")
        self.entry_c1.setClearButtonEnabled(True)
        self.entry_c1.move(50,55+40+40+40+40+40+40)
        self.entry_c1.returnPressed.connect(self.upload)
        
        self.layout_tools.addWidget(self.first_frame)
        
        """ 
            <SecondTabWidget> 
            Data Base View - Objet 
        """
        
        
        """ Add widgets in main window """
        self.mainbox.addWidget(self.first)      # add first widget in mainbox layout.
        self.mainbox.addWidget(self.second)     # add second widget in mainbox layout.
        self.setCentralWidget(self.frame)       # set central widget.
    
    def buildRK1(self):
        """ Runge Kutta 1 """
        self.resultRK1 , self.realdata = RK1(model, self.Xo, self.Xf, self.Yo, self.n, self.equation, self.step, self.constant)
        self.table_rk1 = QTableWidget(self.resultRK1.shape[0],6)
        
        headerLabels = [
        'Xn',
        'Yn ó Y1',
        'Yn+1',
        'Y',
        '|Y-Yn|',
        '|Y-Yn|*100/Y']
        
        self.table_rk1.setHorizontalHeaderLabels(headerLabels)
        #self.table_rk1.setFixedWidth(800)
        self.table_rk1.setFixedHeight(200)
        
        for row in range(0,self.resultRK1.shape[0],1):
            self.table_rk1.setItem(row, 3, QTableWidgetItem(str(self.realdata[0][row])))
            for col in range(1,self.resultRK1.shape[1],1):
                self.table_rk1.setItem(row, col-1, QTableWidgetItem(str(self.resultRK1[row][col])))
    def buildRK2(self):
        """ Runge Kutta 2 """
        self.resultRK2 = RK2(model, self.Xo, self.Xf, self.Yo, self.n, self.step, self.constant)
        self.table_rk2 = QTableWidget(self.resultRK2.shape[0],8)
        
        headerLabels = [
        'Xn',
        'Yn ó Y2',
        'K1',
        'K2',
        'Yn+1',
        'Y',
        '|Y-Yn|',
        '|Y-Yn|*100/Y']
        
        self.table_rk2.setHorizontalHeaderLabels(headerLabels)
        self.table_rk2.setFixedHeight(200)
        
        for row in range(0,self.resultRK2.shape[0],1):
            self.table_rk2.setItem(row, 5, QTableWidgetItem(str(self.realdata[0][row])))
            for col in range(1,self.resultRK2.shape[1],1):
                self.table_rk2.setItem(row, col-1, QTableWidgetItem(str(self.resultRK2[row][col])))
                
    def buildRK3(self):
        """ Runge Kutta 3 """
        self.resultRK3 = RK3(model, self.Xo, self.Xf, self.Yo, self.n, self.step, self.constant)
        self.table_rk3 = QTableWidget(self.resultRK3.shape[0],9)
        
        headerLabels = [
            'Xn',
            'Yn ó Y3',
            'K1',
            'K2',
            'K3',
            'Yn+1',
            'Y',
            '|Y-Yn|',
            '|Y-Yn|*100/Y']
        
        self.table_rk3.setHorizontalHeaderLabels(headerLabels)
        self.table_rk3.setFixedHeight(200)
        
        for row in range(0,self.resultRK3.shape[0],1):
            self.table_rk3.setItem(row, 6, QTableWidgetItem(str(self.realdata[0][row])))
            for col in range(1,self.resultRK3.shape[1],1):
                self.table_rk3.setItem(row, col-1, QTableWidgetItem(str(self.resultRK3[row][col])))

    def buildRK4(self):
        """ Runge Kutta 4 """
        self.resultRK4 = RK4(model, self.Xo, self.Xf, self.Yo, self.n, self.step, self.constant)
        self.table_rk4 = QTableWidget(self.resultRK4.shape[0],10)
        
        headerLabels = [
            'Xn',
            'Yn ó Y3',
            'K1',
            'K2',
            'K3',
            'K4',
            'Yn+1',
            'Y',
            '|Y-Yn|',
            '|Y-Yn|*100/Y']
        
        self.table_rk4.setHorizontalHeaderLabels(headerLabels)
        self.table_rk4.setFixedHeight(200)
        
        for row in range(0,self.resultRK4.shape[0],1):
            self.table_rk4.setItem(row, 7, QTableWidgetItem(str(self.realdata[0][row])))
            for col in range(1,self.resultRK4.shape[1],1):
                self.table_rk4.setItem(row, col-1, QTableWidgetItem(str(self.resultRK4[row][col])))                
    
    def upload(self):
        
        """ Upgrade Tables RK's """
        if not self.table_enable:
            print("upload")
            self.layout_table_rk1 = QVBoxLayout(self.second.tab1)
            self.layout_table_rk2 = QVBoxLayout(self.second.tab2)
            self.layout_table_rk3 = QVBoxLayout(self.second.tab3)
            self.layout_table_rk4 = QVBoxLayout(self.second.tab4)
            
            """ Get values for RK """
            self.equation = self.entry_equ.text()
            self.Xo = float(self.entry_xo.text())
            self.Xf = float(self.entry_xf.text())
            self.Yo = float(self.entry_yo.text())
            self.n = int(self.entry_n.text())
            self.step = float(self.entry_h.text())
            self.constant = eval(self.entry_c1.text())
            
            """ Runge Kutta 1 """
            self.buildRK1()               
            
            """ Runge Kutta 2 """
            self.buildRK2()               
            
            """ Runge Kutta 3 """
            self.buildRK3()
            
            """ Runge Kutta 4 """
            self.buildRK4()
            
            self.layout_table_rk1.addWidget(self.table_rk1)
            self.layout_table_rk2.addWidget(self.table_rk2)
            self.layout_table_rk3.addWidget(self.table_rk3)
            self.layout_table_rk4.addWidget(self.table_rk4)
            
            self.second.tab4.setLayout(self.layout_table_rk4)
            self.second.tab3.setLayout(self.layout_table_rk3)
            self.second.tab2.setLayout(self.layout_table_rk2)
            self.second.tab1.setLayout(self.layout_table_rk1)
            self.table_enable = True
        else:
            print("upload-2")
            self.table_rk1.deleteLater()
            self.table_rk2.deleteLater()
            self.table_rk3.deleteLater()
            self.table_rk4.deleteLater()
            
            self.equation = self.entry_equ.text()
            self.Xo = float(self.entry_xo.text())
            self.Xf = float(self.entry_xf.text())
            self.Yo = float(self.entry_yo.text())
            self.n = int(self.entry_n.text())
            self.step = float(self.entry_h.text())
            self.constant = eval(self.entry_c1.text())
            
            """ Runge Kutta 1 """
            self.buildRK1()               
            
            """ Runge Kutta 2 """
            self.buildRK2()               
            
            """ Runge Kutta 3 """
            self.buildRK3()
            
            """ Runge Kutta 4 """
            self.buildRK4()

            self.layout_table_rk1.addWidget(self.table_rk1)
            self.layout_table_rk2.addWidget(self.table_rk2)
            self.layout_table_rk3.addWidget(self.table_rk3)
            self.layout_table_rk4.addWidget(self.table_rk4)
            
            self.second.tab4.setLayout(self.layout_table_rk4)
            self.second.tab3.setLayout(self.layout_table_rk3)
            self.second.tab2.setLayout(self.layout_table_rk2)
            self.second.tab1.setLayout(self.layout_table_rk1)
            self.table_enable = True
            
""" Main """

if __name__ == '__main__':
    Appx = QApplication(sys.argv)

    mainWindow = AppMain()
    mainWindow.show()

    sys.exit(Appx.exec())

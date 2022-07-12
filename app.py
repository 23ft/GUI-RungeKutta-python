from PySide6.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                               QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QMenu, QTabWidget, QComboBox)
from PySide6.QtCore import Qt, QSize, QPointF, QRect
from PySide6.QtGui import QLinearGradient, QPalette, QColor, QIcon, QPixmap, QFont
from styles.style import *

import sys


""" OBjeto pestañas """


class MyTabWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        self.tab1 = QWidget()    # Primera pestaña, se pasa como widget.
        self.tab1.setStyleSheet("""
                                    background-color: gray;

                                """)

        self.tab2 = QWidget()   # Segunda pestaña, se pasa como widget.
        self.tab3 = QWidget()   # Tercera pestaña, se pasa como widget.

        self.tabs.resize(300, 200)
        self.tabs.setStyleSheet("""
                                    background-color:#eee;
                                    margin: 5px;
                                
                                """)

        self.tabs.addTab(self.tab1, "Geeks")
        self.tabs.addTab(self.tab2, "For")
        self.tabs.addTab(self.tab3, "Geeks")  # Añadimos pestañas a tabs.

        # creacion boton como hijo de tab1.
        self.btn_menu = QPushButton(parent=self.tab1, text="Connection")
        self.btn_menu.setObjectName("btn_menu")
        self.btn_menu.setStyleSheet(btn_menu_css)
        self.btn_menu.setGeometry(QRect(0, 0, 100, 40))
        self.btn_menu.setCheckable(True)
        self.btn_menu.clicked.connect(self.menuHand)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def menuHand(self):
        print("pepe")


""" Ventana Principal """


class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = 1000
        self.h = 500

        # self.setAutoFillBackground(True)
        self.setFixedSize(self.w, self.h)
        #self.setGeometry(500, 200, 300, 250)
        self.setStyleSheet(main_css)
        self.mainbox = QVBoxLayout()

        self.setCentralWidget(MyTabWidget(self))


""" Ventana Login """


class AppLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = 400
        self.h = 380
        self.setFixedSize(self.w, self.h)
        self.setWindowTitle("Order Components DB")

        # self.setWindowOpacity(0.5)
        # self.setStyleSheet(main_css)

        self.initUi()

    def initUi(self):
        """ Instanciamos las ventanas del programa """
        self.mainScreen = AppMain()

        """ HEADER """
        frame = QFrame(self)
        frame.setObjectName("header")
        frame.setStyleSheet(login_css)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setFixedWidth(400)
        frame.setFixedHeight(84)

        self.vbox = QVBoxLayout(frame)          # layout, hijo de frame.
        self.vbox.setAlignment(Qt.AlignCenter)  # definicimos la alineacion.

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(16)
        fuenteTitulo.setBold(True)
        labelTitulo = QLabel("<font color='white'> Base Datos </font>")
        labelTitulo.setFont(fuenteTitulo)
        #labelTitulo.move(150, 20)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(9)
        labelSubtitulo = QLabel("<div> 23ft </div>")
        labelSubtitulo.setObjectName("login_23ft")
        labelSubtitulo.setStyleSheet(login_css)
        labelSubtitulo.setFont(fuenteSubtitulo)
        #labelSubtitulo.move(200, 46)

        self.vbox.addWidget(labelTitulo)
        self.vbox.addWidget(labelSubtitulo)

        """ BODY """
        self.labelCuenta = QLabel("Cuenta", self)
        self.labelCuenta.setStyleSheet("color: #111;")
        self.labelCuenta.move(60, 110)

        self.comboBoxCuenta = QComboBox(self)
        self.comboBoxCuenta.addItems(["Administrador", "Usuario"])
        self.comboBoxCuenta.setCurrentIndex(-1)
        self.comboBoxCuenta.setFixedWidth(280)
        self.comboBoxCuenta.setFixedHeight(26)
        self.comboBoxCuenta.move(60, 136)

        # USUARIO.
        labelUsuario = QLabel("Usuario", self)
        labelUsuario.move(60, 170)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(60, 196)

        #imagenUsuario = QLabel(frameUsuario)
        # imagenUsuario.setPixmap(QPixmap("usuario.png").scaled(20, 20, Qt.KeepAspectRatio,
        #                                                      Qt.SmoothTransformation))
        # imagenUsuari   o.move(10, 4)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.setStyleSheet("border-radious: 60px")
        self.lineEditUsuario.move(40, 1)

        # CONTRASEÑA.

        self.label_pass = QLabel("Contraseña", self)

        self.label_pass.move(60, 224)

        self.framePass = QFrame(self)
        self.framePass.setFrameShape(QFrame.StyledPanel)
        self.framePass.setFixedWidth(280)
        self.framePass.setFixedHeight(28)
        self.framePass.move(60, 250)

        #imagenContrasenia = QLabel(frameContrasenia)
        # imagenContrasenia.setPixmap(QPixmap("contraseña.png").scaled(20, 20, Qt.KeepAspectRatio,
        # Qt.SmoothTransformation))
        #imagenContrasenia.move(10, 4)

        self.lineEditPass = QLineEdit(self.framePass)
        self.lineEditPass.setFrame(False)
        self.lineEditPass.setEchoMode(QLineEdit.Password)
        self.lineEditPass.setTextMargins(8, 0, 4, 1)
        self.lineEditPass.setFixedWidth(238)
        self.lineEditPass.setFixedHeight(26)
        self.lineEditPass.move(40, 1)
        
        # Buttons   
        
        self.button_submit = QPushButton("Submit", self)
        self.button_submit.setObjectName("button_submit")
        self.button_submit.setFixedWidth(135)
        self.button_submit.setFixedHeight(28)
        self.button_submit.move(60, 286)
        
        self.button_submit.clicked.connect(self.submit) 
        
        
        self.button_exit = QPushButton("Exit", self)
        self.button_exit.setObjectName("button_exit")
        self.button_exit.setFixedWidth(135)
        self.button_exit.setFixedHeight(28)
        self.button_exit.move(205, 286) 
        
        self.button_exit.clicked.connect(self.exit)
        
        
    """ Callback function for the buttons"""    

    def submit(self):
        # corroborar usuarios.
        #self.close()            # close hace uso de destroy.
        #self.mainScreen.show()  # mostramos ventana nueva.
        
        print(self.lineEditUsuario.text())

    def exit(self):
        print("Exit")
        self.close()    

if __name__ == '__main__':
    Appx = QApplication()

    mainWindow = AppLogin()
    mainWindow.show()

    sys.exit(Appx.exec())

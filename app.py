from PySide6.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                               QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QMenu, QTabWidget, QComboBox)
from PySide6.QtCore import Qt, QSize, QPointF, QRect
from PySide6.QtGui import QLinearGradient, QPalette, QColor, QIcon, QPixmap, QFont
from styles.style import *

import sys


""" Personal Objets """


class SecondTabWidget(QWidget):
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

        self.tabs.setFixedWidth(800)
        self.tabs.setStyleSheet("""
                                    background-color:#eee;
                                    margin: 5px;
                                
                                """)

        self.tabs.addTab(self.tab1, "Resisencias")
        self.tabs.addTab(self.tab2, "Transistores")
        self.tabs.addTab(self.tab3, "Modulos-PCB")  # Añadimos pestañas a tabs.

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class FirstTabWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        self.tab1 = QWidget()    # Primera pestaña, se pasa como widget.
        self.tab1.setStyleSheet("""
                                    background-color: gray;

                                """)

        self.tab2 = QWidget()   # Segunda pestaña, se pasa como widget.
        # self.tab3 = QWidget()   # Tercera pestaña, se pasa como widget.

        self.tabs.setFixedWidth(380)
        self.tabs.setStyleSheet("""
                                    background-color:#eee;
                                    margin: 5px;
                                
                                """)

        self.tabs.addTab(self.tab1, "Insertar")
        self.tabs.addTab(self.tab2, "Borrar")
        # self.tabs.addTab(self.tab3, "Geeks")  # Añadimos pestañas a tabs.

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def menuHand(self):
        print("pepe")


class BoxModel(QWidget):
    def __init__(self, referencia, cantidad):
        super().__init__()
        """ Creando boxmodel elementos inventario """
        # self.setAutoFillBackground(True)

        #self.boxdb = QWidget()
        self.dispose = QVBoxLayout()

        self.dispose.addWidget(QLabel("Imagen"))  # imagen elemento.
        referencia = ">> " + referencia + "\n>> " + cantidad
        self.dispose.addWidget(QLabel(referencia))
        self.setLayout(self.dispose)


class SheapDB(QWidget):
    def __init__(self):
        super().__init__()
        self.content = BoxModel("Resistencia 10K", "50")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.content)

        self.setLayout(self.layout)

        self.setAutoFillBackground(True)
        self.setFixedSize(QSize(210, 210))
        self.setStyleSheet("""
                           background-color: #aaa;
                           border: 2px ridge #000;
                           padding: 10px;
                           """)


""" Ventana Principal """


class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()

        # Widget that contains the collection of Vertical Box
        self.widget = QWidget()
        self.container = QWidget()
        # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.vbox = QVBoxLayout()
        self.box = QHBoxLayout()            # layout primaria.

        self.w = 1300
        self.h = 500

        # self.setAutoFillBackground(True)
        self.setFixedSize(self.w, self.h)
        #self.setGeometry(500, 200, 300, 250)
        self.setStyleSheet(main_css)
        self.initUi()

    def initUi(self):

        self.frame = QFrame(self)
        self.frame.setObjectName("AppMainFrame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setAutoFillBackground(True)
        self.frame.setFixedWidth(self.w)
        self.frame.setFixedHeight(self.h)

        self.mainbox = QHBoxLayout(self.frame)
        self.first = FirstTabWidget(self.mainbox)
        self.second = SecondTabWidget(self.mainbox)

        self.objFrame = QFrame(self.first.tab1)
        self.objFrame.setFrameShape(QFrame.NoFrame)
        self.objFrame.setFrameShadow(QFrame.Sunken)
        self.objFrame.setAutoFillBackground(True)
        self.objFrame.setFixedWidth(300)
        self.objFrame.setFixedHeight(300)
        self.objFrame.setStyleSheet("background-color: black")
        # self.objFrame.move(100,100)

        """ Scroll """
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        for i in range(1, 50):
            object = SheapDB()
            self.vbox.addWidget(object)

        # seteamos la plantilla en el widget widget.
        self.widget.setLayout(self.vbox)

        """ Gestion scrollbar """
        # Scroll Area Properties
        # Scroll Area which contains the widgets, set as the centralWidget
        self.scroll = QScrollArea(self.second.tab1)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.mainbox.addWidget(self.first)
        self.mainbox.addWidget(self.second)

        self.setCentralWidget(self.frame)


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
        self.close()            # close hace uso de destroy.
        self.mainScreen.show()  # mostramos ventana nueva.

        # print(self.lineEditUsuario.text())

    def exit(self):
        print("Exit")
        self.close()


if __name__ == '__main__':
    Appx = QApplication()

    mainWindow = AppLogin()
    mainWindow.show()

    sys.exit(Appx.exec())

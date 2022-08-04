from PySide6.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                               QHBoxLayout, QVBoxLayout, QBoxLayout, QMainWindow, QFrame, QMenu, QTabWidget, QComboBox, QGridLayout)
from PySide6.QtCore import Qt, QSize, QPointF, QRect, QMargins
from PySide6.QtGui import QLinearGradient, QPalette, QColor, QIcon, QPixmap, QFont

from styles.style import *
from lib.database.driver import *
import sys

""" App Objets - App Widgets """


class SecondTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        # layout para el objeto SecondTabWidget.
        self.layout = QVBoxLayout(self)

        # Instacia QtabWidget.
        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        self.tabs.setFixedWidth(800)
        self.tabs.setStyleSheet("""
                                    QTabWidget::pane { /* The tab widget frame */
                                        border: 1px solid #C2C7CB;
                                        position: absolute;
                                        top: -0.5em;
                                        
                                    }

                                    QTabWidget::tab-bar {
                                        /*alignment: center;*/
                                     }

                                     /* Style the tab using the tab sub-control. Note that
                                         it reads QTabBar _not_ QTabWidget */
                                     QTabBar::tab {
                                         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
                                         border: 2px solid #B2B2B2;
                                         border-bottom-color: #B2B2B2; /* same as the pane color */
                                         border-top-left-radius: 4px;
                                         border-top-right-radius: 4px;
                                         min-width: 8ex;
                                         padding: 2px;
                                     }

                                     QTabBar::tab:selected, QTabBar::tab:hover {
                                         /*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                     stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                                                     stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);*/
                                        background-color: #B2B2B2;                                                                     
                                     }

                                     QTabBar::tab:selected {
                                         border-color: #B2B2B2;
                                         border-bottom-color: #AD85BA; /* same as pane color */
                                     }

                                """)

        # pestaña 1
        self.tab1 = QFrame(self)    # Primera pestaña, se pasa como widget.
        # self.tab1.setFrameShape(QFrame.NoFrame)
        # self.tab1.setFrameShadow(QFrame.Sunken)
        self.tab1.setAutoFillBackground(True)
        self.tab1.setStyleSheet("""
                                    background-color: #B2B2B2;
                                    
                                """)

        # pestaña 2
        self.tab2 = QWidget()   # Segunda pestaña, se pasa como widget.

        # pestaña 3
        self.tab3 = QWidget()   # Tercera pestaña, se pasa como widget.

        # Add new tabs in QtabWidget.
        self.tabs.addTab(self.tab1, "Resisencias")
        self.tabs.addTab(self.tab2, "Transistores")
        self.tabs.addTab(self.tab3, "Modulos-PCB")  # Añadimos pestañas a tabs.

        # añadimos el widget en layout de SecondTabWidget.
        self.layout.addWidget(self.tabs)

        # definimos el layout.
        self.setLayout(self.layout)


class FirstTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        
        
        self.tab1 = QWidget()    # Primera pestaña, se pasa como widget.
        self.tab1.setObjectName("tab1_firts")
        

        self.tab2 = QWidget()   # Segunda pestaña, se pasa como widget.
        # self.tab3 = QWidget()   # Tercera pestaña, se pasa como widget.

        #self.tabs.setFixedWidth(380)
        self.tabs.setStyleSheet("""
                                    background-color: #B2B2B2;

                                """)

        self.tabs.addTab(self.tab1, "Insertar")
        self.tabs.addTab(self.tab2, "Borrar")
        # self.tabs.addTab(self.tab3, "Geeks")  # Añadimos pestañas a tabs.

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def menuHand(self):
        print("pepe")


class BoxModel(QFrame):
    def __init__(self, referencia, cantidad):
        super().__init__()
        """ Creando boxmodel elementos inventario """
        # self.setAutoFillBackground(True)

        # Layout para registro base datos.
        self.dispose = QVBoxLayout()

        # medidas
        self.w = 210
        self.h = 210

        # diseño frame
        # self.setObjectName("BoxModel")
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Sunken)
        self.setAutoFillBackground(True)
        self.setFixedWidth(self.w)
        self.setFixedHeight(self.h)
        self.setStyleSheet("""background-color: #000;
                              color: #FFF;
                           """)

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


""" App Widnows """


class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        """ Propieties AppMain """
        self.widget_db = QWidget()          # widget for storage grid layout.
        self.grid_layout = QGridLayout()    # grid layout for data base registers.
        self.rows = None        # rows in grid layout.
        self.Columns = None     # columns in grid layout.
        self.w = 1240           # width window.
        self.h = 480            # height window.
        
        """ Configuration AppMain"""
        self.setWindowTitle("Control Inventary - 23ft")
        self.setFixedSize(self.w, self.h)   # config initial size.
        self.setStyleSheet(main_css)        # define style sheet
        
        """ Database Configuration """
        self.port=6603,
        self.host="198.58.99.52",
        self.user="root",
        self.password="8;Ud1V.7jm2_C#&y.9X?NzZ0RdM_t2j2"
        
        self.streamDB = databaseDrive(self.port, self.host, self.user,self.password)
         
        
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
        
        self.first.tabs.setFixedWidth(300)      
        """ 
            <FirstTabWidget>
            Actions Data Base 
        """
        self.layout_tools = QVBoxLayout()
        self.pepe = QBoxLayout()
        self.layout_tools.setContentsMargins(0,0,0,0)   # quitar magins del layout.
        self.layout_tools.setAlignment(Qt.AlignVCenter)
        
        
        self.first_frame = QFrame()
        self.second_frame = QFrame()
        self.second_frame.setObjectName("pepe")
        self.second_frame.setFixedWidth(300)
        self.second_frame.setStyleSheet("""
                                            #pepe{
                                                margin: 0px;

                                            }
                                        """)
        
        self.second_frame.setFrameShape(QFrame.NoFrame)
        self.second_frame.setFrameShadow(QFrame.Sunken)
        self.second_frame.setAutoFillBackground(True)
        self.second_frame.width()
        #self.objFrame.setStyleSheet("background-color: #B2B2B2")
        #self.frame_insert.addWidget(self.objFrame)
        
        self.label_pass = QLabel("Categoria:", self.first_frame)
        #self.label_pass.move(30, 4)
        
        self.comboBoxCuenta = QComboBox(self.first_frame)
        self.comboBoxCuenta.addItems(["Resistenica", "Semiconductor", "Modulo Framework - PCB"])
        #self.comboBoxCuenta.setCurrentIndex(-1)
        #self.comboBoxCuenta.setMinimumWidth(280)
        #self.comboBoxCuenta.setMinimumHeight(26)
        self.comboBoxCuenta.move(0, 30)
        
        self.button_insert = QPushButton("Insert", self.second_frame)
        self.button_insert.setObjectName("button_insert")
        self.button_insert.setFixedWidth(135)
        self.button_insert.setFixedHeight(28)
        self.button_insert.move(int(self.second_frame.width() / 2) - int(self.button_insert.width() / 2), 0)

        
        

        #self.frame_insert.addWidget(self.label_pass)
        #self.frame_insert.addWidget(self.comboBoxCuenta)
        #self.layout_tools.addStretch()
        self.layout_tools.addWidget(self.first_frame)
        self.layout_tools.addWidget(self.second_frame)
        self.first.tab1.setLayout(self.layout_tools)
        
        
        
        #self.layout_tools.addStretch()
        """ 
            <SecondTabWidget> 
            Data Base View - Objet 
        """
        # Ajustando grilla para visualizacion registros DB en modo GRID.
        for row in range(0, 50, 2):
            self.grid_layout.setRowMinimumHeight(row, 25)
            for column in range(0, 7, 2):
                self.grid_layout.setColumnMinimumWidth(column, 25)

        # Insertando registros de base de datos.
        for row in range(1, 50, 2):
            for column in range(1, 9, 2):
                object = BoxModel("Resistencia 10K", "50")      # BoxModel is objet for data base register.
                self.grid_layout.addWidget(object, row, column) # Add BoxModel with data base register in the grid.

        # seteamos la plantilla en el widget widget.
        self.widget_db.setLayout(self.grid_layout)

        """ 
            <ScrollArea>
            ScrollArea for view data base registrers
        """        
        self.scroll_layout = QHBoxLayout(self.second.tab1)                 # layout for scrollArea, parent is tab1.        
        self.scroll_db = QScrollArea()                                     # instancia QscrollArea
        self.scroll_db.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)    # enable vertical scrollbar
        self.scroll_db.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # enable horizontal scrollbar 
        self.scroll_db.setWidgetResizable(True)                            # enable resizable
        self.scroll_db.setWidget(self.widget_db)                           # wdiget dentro de ScrollArea
        self.scroll_db.setStyleSheet("""
                                     /* ScrollBar */
                                        
                                        
                                        /* ScrollArea */
                                     
                                        QScrollArea {
                                            background-color: #B2B2B2;
                                            border: 0px;
                                        }
                                        
                                        
                                     """)               # Dentro de ScrollArea encontramos objetos como QscrollBar.

        
        self.scroll_layout.addWidget(self.scroll_db)    # add scrollarea to scroll layout.

        """ Add widgets in main window """
        self.mainbox.addWidget(self.first)      # add first widget in mainbox layout.
        self.mainbox.addWidget(self.second)     # add second widget in mainbox layout.
        self.setCentralWidget(self.frame)       # set central widget.
        
        


""" Ventana Login """


class AppLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = 400
        self.h = 380
        self.setFixedSize(self.w, self.h)
        self.setWindowTitle("Control Inventary - 23ft")

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
        # labelTitulo.move(150, 20)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(9)
        labelSubtitulo = QLabel("<div> 23ft </div>")
        labelSubtitulo.setObjectName("login_23ft")
        labelSubtitulo.setStyleSheet(login_css)
        labelSubtitulo.setFont(fuenteSubtitulo)
        # labelSubtitulo.move(200, 46)

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

        # imagenUsuario = QLabel(frameUsuario)
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

        # imagenContrasenia = QLabel(frameContrasenia)
        # imagenContrasenia.setPixmap(QPixmap("contraseña.png").scaled(20, 20, Qt.KeepAspectRatio,
        # Qt.SmoothTransformation))
        # imagenContrasenia.move(10, 4)

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


""" Main """

if __name__ == '__main__':
    Appx = QApplication()

    mainWindow = AppLogin()
    mainWindow.show()

    sys.exit(Appx.exec())

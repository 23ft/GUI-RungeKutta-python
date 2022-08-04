from getpass import getpass
from mysql.connector import connect, Error
#from query import *
"""

    clave root DataBase debian: 8;Ud1V.7jm2_C#&y.9X?NzZ0RdM_t2j2
    
    ****
    Documentacion:
    
    Crear tablas SQL - Microsoft -> https://docs.microsoft.com/es-es/sql/t-sql/lesson-1-creating-database-objects?view=sql-server-ver16
    
    ****
    
    cmd docker:
    
        -> docker ps (view dockers already running)
        -> docker exec -it "docker-name" bash (correr bash en contenedor seleccionado)
        
    cmd mysql:

        -> mysql -uroot -p (iniciar mysql como root)
 
"""

# Variables globales.
TABLES = {} # diccionario tablas creadas inventario_2022
QUERY = {}  # diccionario con query para SQL


QUERY["insert_table"] = """
INSERT inventario_2022.Resistencias VALUES (0, "180Komh", 40)

"""

# Creacion tabla.
TABLES['first_table'] = """
CREATE TABLE IF NOT EXISTS inventario_2022.Resistencias (
    ResistorID int PRIMARY KEY NOT NULL,
    ResistorReferencia varchar(20) NOT NULL,
    ResistorStock int NOT NULL
)
"""


TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")


class databaseDrive():
    def __init__(self, port, host, user, password):
        self.port = port
        self.host = host
        self.user = user
        self.password = password
        
        self.database = None
        self.connection = None  # connection to database
        
    def send(self, query):
        try:
        
            # Establecer conexcion con connect como connection, el valor devuleto es el objeto de la conexion.
            # Recomendable con 'with' para no dejar conexiones abiertas.
            with connect(
                port=self.port,
                host=self.host,
                user=self.user,
                password=self.password, 
            ) as conn:
                self.connection = conn
                #print(TABLES)                
                #withCursor(connection, "")        
                #withCursor(connection, TABLES["first_table"])        
                self.withCursor(query)   

        except Error as e:    
            print(e)
    
    def commit(self):
        self.connection.commit()  # cada efecto realizado hay que actualizarlo con ayuda del commit, metodo en el objeto de conexion.
        
    def withCursor(self, query):
        with self.connection.cursor() as cursor:
            
            cursor.execute(query) # Para ejecutar las peticiones es necesario el cursor.
            self.commit()
            #print(cursor)
            #for db in cursor:
            #    pass
            #    #print("\n", len(db))
            




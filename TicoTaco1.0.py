###############################################################################################
#                                                                                             #
#                        TICO-TACO (TIC-TAC-TOE ORIENTADO A OBJETOS)                          #                            
#                                                                                             #
#               Version 1.0      Fecha 19MAY2022     Autor Eduardo Robledo                    #
#                                                                                             #
#  Fruto del aburrimiento y el exceso de tiempo libre decidi mejorar el tic-tac-toe en modo   #
#  texto y adaptarlo a la programacion orientada a objetos                                    #
#                                                                                             #
###############################################################################################

# Importamos librerias: rando.randrange nos ayudara a realizar movimientos aleatorios con la 
# IA, mientras que time.sleep() se usara para tener una presentacion mas amigable

from random import randrange
from time import sleep

###############################################################################################
#                                                                                             #
# Clase Casilla                                                                               #
#                                                                                             #
# Version: 1.0      Fecha 19MAY2022     Autor: Eduardo Robledo                                #
#                                                                                             #
# Comprende cada una de las casillas del tablero, En su constructor, recibe un numero, que se #
# asignara a la variable de instancia 'numero' y se establece su signo a None, es decir, esta #
# vacia en el momento de se creacion. Ademas, se crean metodos para asignarle un signo        #
# (set()), leer su estado (get()) y mostrar el su contenido como una cadena de texto          #
# (toText())                                                                                  #
#                                                                                             #
###############################################################################################
class Casilla:
    def __init__(self, numero):
        self.numero = numero
        self.signo = None
    
    def set(self, signo):
        self.signo = signo
        
    def get(self):
        return self.signo
        
    def toText(self):
        if self.signo == 1:
            return "X"
        if self.signo == 0:
            return "O"
        else:
            return " "

###############################################################################################
#                                                                                             #
# Clase Tablero                                                                               #
#                                                                                             #
# Version: 1.0      Fecha 19MAY2022     Autor: Eduardo Robledo                                #
#                                                                                             #
# Representa el tablero de juego. En su constructor, crea una lista de 9 instancias del la    #
# clase Casilla. Ademas, se crean metodos para asignarle un signo a una casilla (set()), y    #
# leer el estado de una casilla (get()). Estos metodos hacen usos de los metodos get() y      #
# set() de la clase Casilla previamente creados.                                              #
#                                                                                             #
############################################################################################### 
class Tablero:
    def __init__(self):
        self.casilla = [Casilla(i) for i in range(1,10)]
        
    def set(self, i, signo):
        self.casilla[i].set(signo)
        
    def get(self, i):
        return self.casilla[i].get()

############################################################################################### 
#                                                                                             #
# Clase Jugador                                                                               #
#                                                                                             #
# Version 0.1      Fecha 20MAY22        Autor Eduardo Robledo                                 #
#                                                                                             #
# Representa a cada uno de los jugadores. El constructor instancia al objeto con el atributo  #
# signo recibido como parametro. Ademas, hay un metodo get() para obtener el valor de este    #
# atributo. En la version 1.0 de TicoTaco no se utiliza, aunque se implementa para ser        #
# utilizado en futuras versiones.                                                             #
#                                                                                             #
############################################################################################### 
class Jugador:
    def __init__(self, signo):
        self.signo = signo
    def __get(self):
        return self.signo

###############################################################################################
#                                                                                             #
# Funcion mostrarTablero(tablero)                                                             #
#                                                                                             #
# Version 0.9          Fecha 19MAY22           Autor Eduardo Robledo                          #
#                                                                                             #
# @param tablero        El tablero a mostrar                                                  #
# sin retorno                                                                                 #
#                                                                                             #
# Toma el tablero recibido como parametro y lo recorre casilla a casilla, mostrando el        #
# contenido de cada casilla. Incompatible con algunos sandboxes, posiblemente por el uso del  #
# parametro "end" en las llamadas a la funcion print().                                       #
#                                                                                             #
###############################################################################################

def mostrarTablero(tablero):
    print("┌───┬───┬───┐\n| ", end="")
    for i in range(9):
        if i == 3 or i == 6:
            print("\n├───┼───┼───┤\n| ", end="")
        print(tablero.casilla[i].toText(), "", end="| ")
    print("\n└───┴───┴───┘")
    sleep(1)

###############################################################################################
#                                                                                             #
# Funcion jugarTurno(numeroJugadores, turno)                                                  #
#                                                                                             #
# Version 1.0          Fecha 19MAY22           Autor Eduardo Robledo                          #
#                                                                                             #
# @param numeroJugadores        El numero de jugadores de la partida (1/2)                    #
# @param turno                  El jugador que tiene el turno                                 #
# sin retorno                                                                                 #
#                                                                                             #
# Si el numero de jugadores es 1 y es el turno de la IA para jugar, realizara un movimiento   #
# aleatorio, comprobara si esta libre y repitira el proceso hasta que encuentre una casilla   #
# libre. Entonces, usa el metodo set de la casilla marcarla con X.                            #
# Si la partida es de dos jugadores, se pedira al jugador pasado como parametro que           #
# introduzca un movimiento, que se comprobara y repetira el proceso del mismo modo que antes. #
# Si se introduce una casilla libre, se usa el metodo set() de la casilla para marcarla con   #
# la letra del jugador que este jugando el turno.                                             #
#                                                                                             #
# En futuras versiones, se implementara el uso de la clase Jugador para jugar los turnos.     #
#                                                                                             #
###############################################################################################
def jugarTurno(numeroJugadores, turno):
    libre = False
    if numeroJugadores == 1:
        if turno == 1:
            while not libre:
                movimiento = randrange(9)
                libre = estaLibre(movimiento-1)
            tablero.casilla[movimiento-1].set(turno)
        else:
            while not libre:
                print("Jugador", turno+1, end=". ")
                movimiento = int(input("Introduzca su movimiento... "))
                libre = estaLibre(movimiento-1)
            tablero.casilla[movimiento-1].set(turno)

###############################################################################################
#                                                                                             #
# Funcion limpiarPantalla()                                                                   #
#                                                                                             #
# Version 1.0          Fecha 19MAY22           Autor Eduardo Robledo                          #
#                                                                                             #
# sin param                                                                                   #
# sin retorno                                                                                 #
#                                                                                             #
# Simplemente imprime en pantalla 8 lineas en blanco para tener una mejor visualizacion en    #
# algunas consolas.                                                                           #
#                                                                                             #
###############################################################################################
def limpiarPantalla():
    for i in range(8):
        print()

###############################################################################################
#                                                                                             #
# Funcion cambiarTurno(turno)                                                                 #
#                                                                                             #
# Version 1.0          Fecha 19MAY22           Autor Eduardo Robledo                          #
#                                                                                             #
# @param turno      El turno que esta siendo jugado actualmente                               #
# return turno      El turno despues del cambio                                               #
#                                                                                             #
# Funcion sencilla que cambia el valor de la variable turno para alternar los jugadores       #
#                                                                                             #
###############################################################################################       
def cambiarTurno(turno):
    if turno == 1:
        return 0
    if turno == 0:
        return 1

###############################################################################################
#                                                                                             #
# Funcion estaLibre(i)                                                                        #
#                                                                                             #
# Version 1.0          Fecha 19MAY22           Autor Eduardo Robledo                          #
#                                                                                             #
# @param i             Casilla a comprobar                                                    #
# return True/False    Boolean con el estado de la variable                                   #
#                                                                                             #
# Si el signo de la casilla es None, significa que esta libre, en ese caso se devuelve True.  #
# En cualquier otro caso, la casilla esta ocupada y se devuelve False.                        #
#                                                                                             #
# En futuras versiones se integrara esta funcion como parametro de la clase Casilla y se      #
# implementara el uso de la clase Jugador.                                                    #
#                                                                                             #
###############################################################################################
def estaLibre(i):
    if tablero.casilla[i].signo == None:
        return True
    else:
        return False

###############################################################################################
#                                                                                             #
# Funcion comprobarVictoria(tabler)                                                           #
#                                                                                             #
# Version 0.9          Fecha 19MAY22           Autor Eduardo Robledo                          #
#                                                                                             #
# @param tablero        El tablero de juego que se esta comprobando                           #
# return ganador        El jugador que ha ganado                                              #
#                                                                                             #
# Comprueba cada una de las 8 posibles combinaciones ganadoras. Si el valor de las tres       #
# casillas es el mismo, comprueba si es distinto de None, en cuyo caso, uno de los jugadores  #
# ha ganado la partida, devolviendo el valor de una de esas casillas                          #
#                                                                                             #
# En futuras versiones, se comprobara si ha terminado la partida en tablas y se intentara     #
# mejorar el algoritmo para hacerlo menos "fuerza bruta"                                      #
#                                                                                             #
###############################################################################################
def comprobarVictoria(tablero):
    ganador = None
    if tablero.casilla[0].get() == tablero.casilla[1].get() and tablero.casilla[0].get() == tablero.casilla[2].get():
        if tablero.casilla[0].get() != None:
            return tablero.casilla[0].get()
    if tablero.casilla[3].get() == tablero.casilla[4].get() and tablero.casilla[3].get() == tablero.casilla[5].get():
        if tablero.casilla[3].get() != None:
            return tablero.casilla[3].get()
    if tablero.casilla[6].get() == tablero.casilla[7].get() and tablero.casilla[7].get() == tablero.casilla[8].get():
        if tablero.casilla[6].get() != None:
            return tablero.casilla[6].get()
    if tablero.casilla[0].get() == tablero.casilla[3].get() and tablero.casilla[0].get() == tablero.casilla[6].get():
        if tablero.casilla[0].get() != None:
            return tablero.casilla[0].get()
    if tablero.casilla[1].get() == tablero.casilla[4].get() and tablero.casilla[1].get() == tablero.casilla[7].get():
        if tablero.casilla[1].get() != None:
            return tablero.casilla[1].get()
    if tablero.casilla[2].get() == tablero.casilla[5].get() and tablero.casilla[2].get() == tablero.casilla[8].get():
        if tablero.casilla[2].get() != None:
            return tablero.casilla[2].get()
    if tablero.casilla[0].get() == tablero.casilla[4].get() and tablero.casilla[0].get() == tablero.casilla[8].get():
        if tablero.casilla[0].get() != None:
            return tablero.casilla[0].get()
    if tablero.casilla[2].get() == tablero.casilla[4].get() and tablero.casilla[2].get() == tablero.casilla[6].get():
        if tablero.casilla[2].get() != None:
            return tablero.casilla[2].get()
    
###############################################################################################
#                                                                                             #
# Funcion main                                                                                #
#                                                                                             #
# Version 1.0          Fecha 19MAY22           Autor Eduardo Robledo                          #
#                                                                                             #
# sin param                                                                                   #
# sin retorno                                                                                 #
#                                                                                             #
# Bloque principal. En primer lugar pregunta por el numero de jugadores, inicializando una    #
# lista de instancias de la clase jugador con dos jugadores. Crea un tablero, inicializa la   #
# variable victoria a None y da el turno al jugador 2. Si el numero de jugadores es 1, la IA  #
# "juega" su primer movimiento en la casilla central siempre y cambia el turno.               #
# Tras esto, mientras la victoria sea para nadie (None), se limpia la pantalla, se muestra el #
# estado del tablero, se juega el turno del jugador correspondiente, se comprueba si se ha    #
# ganado la partida y se cambia de turno. Por ultimo, si ha habido victoria de alguno de los  #
# jugadores, la partida termina y se muestra el tablero final y un mensaje informando del     #
# ganador de la partida                                                                       #
#                                                                                             #
# En futuras versiones se implementara el uso de la clase Jugador, se validaran las entradas  #
# y se mejorara la interfaz grafica.                                                          #
#                                                                                             #
###############################################################################################
numeroJugadores = int(input("Cuantos jugadores? (1/2)... "))

jugador = [Jugador(i) for i in range(2)]
tablero = Tablero()
victoria = None
turno = 1
if numeroJugadores == 1:
    tablero.set(4,turno)
    turno = cambiarTurno(turno)

while victoria == None:
    limpiarPantalla()
    mostrarTablero(tablero)
    jugarTurno(numeroJugadores, turno)
    victoria = comprobarVictoria(tablero)
    turno = cambiarTurno(turno)

if victoria == 1:
    victoria = "X"
elif victoria == 0:
    victoia = "O"
else:
    victoria = "Nadie"
mostrarTablero(tablero)
print("El ganador es ", victoria)
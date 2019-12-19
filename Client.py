import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print ("Connexion établie avec le serveur sur le port {}".format(port))

num1 = input("Entrer le premier numéro :").encode()
num2 = input("Entrer le deuxième numéro : ").encode()

connexion_avec_serveur.send(num1)
connexion_avec_serveur.send(num2)

print("Choisir un calcul : ")
print("1- Addition")
print("2- Soustraction")
print("3- Multiplication")
print("4- Division")

op = input("Entrer votre choix (1 ; 2 ; 3 ou 4): ").encode()
connexion_avec_serveur.send(op)

print(connexion_avec_serveur.recv(1).decode())


print("Fermeture de la connexion")
connexion_avec_serveur.close()
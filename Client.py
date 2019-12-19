import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print ("Connexion établie avec le serveur sur le port {}".format(port))

num1 = float(input("Entrer le premier numéro :"))
num2 = float(input("Entrer le deuxième numéro : "))

connexion_avec_serveur.send = num1 
connexion_avec_serveur.send = num2

print("Choisir un calcul : ")
print("1- Addition")
print("2- Soustraction")
print("3- Multiplication")
print("4- Division")

op = input("Entrer votre choix (1 ; 2 ; 3 ou 4): ")
connexion_avec_serveur.send = op

connexion_avec_serveur.recv (1)
connexion_avec_serveur.send = b"fin"

print("Fermeture de la connexion")
connexion_avec_serveur.close()
import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

num1 = connexion_avec_client.recv (1).decode()
num2 = connexion_avec_client.recv (1).decode()
op = connexion_avec_client.recv (1).decode()

if op == 1 :
    connexion_avec_client.send(num1 + num2).encode()

elif op == 2 :
    connexion_avec_client.send(num1 - num2).encode()

elif op == 3 :
    connexion_avec_client.send(num1 * num2).encode()

elif op == 4 :
    connexion_avec_client.send(num1 / num2).encode()

else :
    connexion_avec_client.send("Donnée erronnée").encode()

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
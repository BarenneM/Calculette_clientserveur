import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

connexion_avec_client.reciv (1)
connexion_avec_client.reciv (1)
connexion_avec_client.reciv (1)

if op == 1 :
    connexion_avec_client.send (num1 + num2)

elif op == 2 :
    connexion_avec_client.send (num1 - num2)

elif op == 3 :
    connexion_avec_client.send (num1 * num2)

elif op == 4 : 
    connexion_avec_client.send (num1 / num2)

else :
    connexion_avec_client.send ("Donnée erronnée")
    
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
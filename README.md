# Calculette_clientserveur

<h1> Code Client </h1>

* Utilisation d'un code client donné par OpenClassroom dans un terminal :

<pre><code>import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion_avec_serveur.close()</code></pre>

* On modifie ensuite le code afin de crée une calculette qui comunique depuis un client avec un serveur. Le code client se charge de tout ce qui est "entrées". 

On crée deux variables, num1 et num2, et on va demandé à l'utilisateur de rentrer le premier numéro ainsi que le second. 
Puis on les envoit au serveur (par exemple pour num1 : "connexion_avec_serveur.send(num1)"). 

Ensuite on lui propose soit d'additionner, soit de soustraires, soit de multiplier, soit de diviser ces deux nombres. 
Pour cela on lui propose une liste : 
1. Addition
2. Soustraction
3. Multiplication
4. Division

et on lui demande de faire un choix (1, 2, 3 ou 4) et de le rentrer. On enregistre ce choix sous une variable "op" que l'on envoit au serveur.

Une fois que le serveur à fait son travail il renvoit un résultat au client et ce dernier l'affiche pour qu'il soit visible par l'utilisateur : print(connexion_avec_serveur.recv(1).decode())

<h2> Code Serveur </h2>

* Utilisation d'un code serveur donné par OpenClassroom dans un second terminal : 

<pre><code>import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()</code></pre>

* On modifie ensuite ce code pour l'adapter à notre projet. Le serveur se charge de tout ce qui est calcul. 

Le serveur reçoit les valeurs entrées par l'utilisateur (num1 et num2) qu'on enregistre également sour deux variables du même nom. 
Le client nous envoit également quel choix d'opération il à fait grâce à la liste donnée, qu'on enregistre également sous une variable "op".

On fait ensuite une suite de condition qui va permettre de choisir la bonne opération et d'effectuer le bon calcul. 
On envoie le résultat au client. 





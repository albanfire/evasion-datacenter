"""Les énigmes du jeu.

poser_enigme() est déjà prête : sers-t'en pour créer les tiennes.
"""


def poser_enigme(question, bonne_reponse, essais=3):
    """Pose une question au joueur.

    Renvoie True si le joueur trouve la bonne réponse avant
    d'avoir épuisé ses essais, sinon False.
    """
    print(f"\n{question}")
    for essai in range(essais, 0, -1):
        reponse = input(f"Ta réponse ({essai} essai(s)) : ").strip().lower()
        if reponse == bonne_reponse.lower():
            print("Bonne réponse !")
            return True
        print("Ce n'est pas ça.")
    print("Plus d'essais… Réfléchis et reviens plus tard.")
    return False
    
def enigme_onduleur():
    """Un boîtier clignote dans le local technique."""
    return poser_enigme(
        "Un boîtier clignote : « UPS ». Cet appareil alimente les serveurs "
        "en cas de coupure de courant. Comment s'appelle-t-il en français ?",
        "onduleur",
    )

# Exemple d'énigme toute prête, à brancher dans le jeu :
def enigme_digicode():
    """Le code est écrit en binaire sur le post-it du bureau."""
    return poser_enigme(
        "Le digicode affiche : « 0100 0010 0111 ». Quel est le code à 3 chiffres ?",
        "427",
    )
def enigme_mot_de_passe():
    """Un écran de connexion demande le mot de passe de l'administrateur."""
    return poser_enigme(
        "Un écran demande le mot de passe admin. Indice : ce sont les 3 lettres "
        "du système qui traduit un nom de site en adresse IP.",
        "dns",
    )


def enigme_adresse_ip():
    """Une étiquette collée sur un serveur donne une adresse incomplète."""
    return poser_enigme(
        "Une étiquette indique : « 127.0.0.? ». C'est l'adresse qu'un ordinateur "
        "utilise pour se parler à lui-même. Quel nombre manque ?",
        "1",
    )

# TODO issue « Les énigmes » : crée au moins deux autres énigmes.
# Idées : un mot de passe à deviner grâce à un indice,
# un câble de la bonne couleur à brancher, une adresse IP à compléter…

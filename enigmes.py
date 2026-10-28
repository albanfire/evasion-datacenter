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


# Exemple d'énigme toute prête, à brancher dans le jeu :
def enigme_digicode():
    """Le code est écrit en binaire sur le post-it du bureau."""
    return poser_enigme(
        "Le digicode affiche : « 0100 0010 0111 ». Quel est le code à 3 chiffres ?",
        "427",
    )


# TODO issue « Les énigmes » : crée au moins deux autres énigmes.
# Idées : un mot de passe à deviner grâce à un indice,
# un câble de la bonne couleur à brancher, une adresse IP à compléter…

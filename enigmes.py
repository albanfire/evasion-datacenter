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
    
def enigme_cable():
    """Paulin se réveille. Il est complètement bourré et ne sait plus quelle fille il a embrassée hier soir."""
    return poser_enigme(
        "Paulin se réveille. Il est complètement bourré et ne sait plus quelle fille il a embrassée hier soir. Quel fille a t'il embrassée hier soir ? - Perrine, Emma, Laurine, ou personne ? ",
        "Personne",
    )    
def enigme_onduleur():
    """Thomas te demande comment s'appelle la daronne la plus fraiche."""
    return poser_enigme(
        "Thomas te demande comment s'appelle la daronne la plus fraiche. Tu as le choix entre vannessa, Lynda, Nathalie ou Flavie.",
        "Nathalie",
    )

# Exemple d'énigme toute prête, à brancher dans le jeu :
def enigme_digicode():
    """Le code est écrit en binaire sur le post-it du bureau."""
    return poser_enigme(
        "Le code est écrit en binaire sur le post-it du bureau. Le digicode affiche : « 0100 0010 0111 ». Quel est le code à 3 chiffres ?",
        "427",
    )
def enigme_mot_de_passe():
    """Aurelien te demande si son outfit lui va bien"""
    return poser_enigme(
        "Aurelien te demande si son outfit lui va bien. Répond oui ou non.",
        "non",
    )


def enigme_adresse_ip():
    """Quel est le bodycount de Lucas ?"""
    return poser_enigme(
        "Quel est le bodycount de Lucas ? cette question est très difficile. cela demande de la concentration.",
        "0",
    )

# TODO issue « Les énigmes » : crée au moins deux autres énigmes.
# Idées : un mot de passe à deviner grâce à un indice,
# un câble de la bonne couleur à brancher, une adresse IP à compléter…

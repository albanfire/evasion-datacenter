"""Évasion du datacenter : point d'entrée du jeu.

Lance le jeu avec :  python main.py
"""

from moteur import Jeu


def main():
    jeu = Jeu("salles.json")
    jeu.afficher_intro()

    # Boucle principale : on lit une commande, on l'exécute, on recommence.
    while jeu.en_cours:
        commande = input("\n> ").strip().lower()
        jeu.executer(commande)


if __name__ == "__main__":
    main()

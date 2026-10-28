"""Le moteur du jeu : l'état de la partie et les commandes du joueur.

Cherche les commentaires « TODO » : chacun correspond à une issue
et à une branche.
"""

import json


class Jeu:
    def __init__(self, fichier_salles):
        # On charge la carte du jeu depuis le fichier JSON.
        with open(fichier_salles, encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        self.salles = donnees["salles"]
        self.salle_actuelle = donnees["depart"]
        self.inventaire = []
        self.en_cours = True

        # TODO issue « Compte à rebours » : retenir l'heure de début.

    def salle(self):
        """Renvoie la salle dans laquelle se trouve le joueur."""
        return self.salles[self.salle_actuelle]

    # ---------------------------------------------------------
    # Lecture des commandes
    # ---------------------------------------------------------
    def executer(self, commande):
        """Découpe la commande en un verbe et un complément, puis agit."""
        if not commande:
            return

        # TODO issue « Compte à rebours » : vérifier le temps restant ici.

        mots = commande.split(maxsplit=1)
        verbe = mots[0]
        complement = mots[1] if len(mots) > 1 else ""

        if verbe == "regarder":
            self.regarder()
        elif verbe == "aide":
            self.aide()
        elif verbe == "quitter":
            self.quitter()
        elif verbe == "aller":
            self.aller(complement)

        # TODO issue « Se déplacer »         : aller <direction>
        # TODO issue « Ramasser des objets »  : prendre <objet>, inventaire
        # TODO issue « Utiliser un objet »    : utiliser <objet>
        # TODO issue « Sauvegarder la partie » : sauver, charger
        else:
            print("Je ne comprends pas. Tape « aide » pour voir les commandes.")

    # ---------------------------------------------------------
    # Commandes déjà prêtes
    # ---------------------------------------------------------
    def afficher_intro(self):
        print("=" * 50)
        print("  ÉVASION DU DATACENTER")
        print("=" * 50)
        print("Tu t'es endormi pendant une intervention de nuit.")
        print("Le datacenter est verrouillé. Trouve la sortie !")
        print("Tape « aide » pour voir les commandes.")
        self.regarder()

    def regarder(self):
        salle = self.salle()
        print(f"\n== {salle['nom']} ==")
        print(salle["description"])
        if salle["objets"]:
            print("Tu vois :", ", ".join(salle["objets"]))
        print("Sorties :", ", ".join(salle["sorties"]))
    
    def aller(self, direction):
        salle = self.salle()
        if direction not in salle["sorties"]:
            print("Tu ne peux pas aller par là.")
            return
        self.salle_actuelle = salle["sorties"][direction]
        self.regarder()

    def aide(self):
        print("Commandes disponibles :")
        print("  regarder           décrit la salle")
        print("  aide               affiche cette aide")
        print("  quitter            quitte le jeu")
        print("  aller <direction>  : se déplacer (nord, sud, est, ouest)")
        # TODO : ajoute ici chaque nouvelle commande que tu crées.

    def quitter(self):
        print("À bientôt !")
        self.en_cours = False

    # ---------------------------------------------------------
    # Commandes à écrire
    # ---------------------------------------------------------
    # TODO issue « Se déplacer » : méthode aller(self, direction)
    # TODO issue « Ramasser des objets » : méthodes prendre(self, objet)
    #      et afficher_inventaire(self)
    # TODO issue « Utiliser un objet » : méthode utiliser(self, objet)

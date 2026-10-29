"""Le moteur du jeu : l'état de la partie et les commandes du joueur.

Cherche les commentaires « TODO » : chacun correspond à une issue
et à une branche.
"""

import json
import time

DUREE_MAX = 15*60  # en secondes

class Jeu:
    def __init__(self, fichier_salles):
        # On charge la carte du jeu depuis le fichier JSON.
        with open(fichier_salles, encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        self.salles = donnees["salles"]
        self.salle_actuelle = donnees["depart"]
        self.inventaire = []
        self.en_cours = True
        self.debut = time.time()
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

        restant = DUREE_MAX - (time.time() - self.debut)
        if restant <= 0:
            print("L'alarme se déclenche… Les vigiles arrivent. Perdu !")
            self.en_cours = False
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
        elif verbe == "prendre":
            self.prendre(complement)
        elif verbe == "inventaire":
            self.afficher_inventaire()
        elif verbe == "utiliser":
            self.utiliser(complement)
        elif verbe == "temps":
            self.temps()

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
        if direction in salle.get("verrous", {}):
            print("La porte est verrouillée.")
            return
        self.salle_actuelle = salle["sorties"][direction]
        self.regarder()
  
    def prendre(self, objet):
        objets = self.salle()["objets"]
        if objet in objets:
            objets.remove(objet)
            self.inventaire.append(objet)
            print(f"Tu prends : {objet}.")
        else:
            print("Cet objet n'est pas ici.")

    def utiliser(self, objet):
        if objet not in self.inventaire:
            print("Tu n'as pas cet objet.")
            return
        verrous = self.salle().get("verrous", {})
        for direction, objet_requis in list(verrous.items()):
            if objet_requis == objet:
                del verrous[direction]
                print(f"La porte {direction} s'ouvre !")
                return
        print("Ça ne sert à rien ici.")
    
    def afficher_inventaire(self):
        if self.inventaire:
            print("Tu as :", ", ".join(self.inventaire))
        else:
            print("Ton inventaire est vide.")
    
    def aide(self):
        print("Commandes disponibles :")
        print("  regarder           décrit la salle")
        print("  aide               affiche cette aide")
        print("  quitter            quitte le jeu")
        print("  aller <direction>  : se déplacer (nord, sud, est, ouest)")
        print("  prendre <objet>    ramasse un objet")
        print("  inventaire         affiche ce que tu portes")
        print("  utiliser <objet>   utilise un objet de ton inventaire")
        print("  temps              affiche le temps restant")
        # TODO : ajoute ici chaque nouvelle commande que tu crées.

    def quitter(self):
        print("À bientôt !")
        self.en_cours = False
    def temps(self):
        restant = max(0, int(DUREE_MAX - (time.time() - self.debut)))
        print(f"Temps restant : {restant // 60} min {restant % 60} s.")

    # ---------------------------------------------------------
    # Commandes à écrire
    # ---------------------------------------------------------
    # TODO issue « Se déplacer » : méthode aller(self, direction)
    # TODO issue « Ramasser des objets » : méthodes prendre(self, objet)
    #      et afficher_inventaire(self)
    # TODO issue « Utiliser un objet » : méthode utiliser(self, objet)

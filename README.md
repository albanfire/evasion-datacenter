# evasion-datacenter
 premier jeu 
# Évasion du datacenter

Un jeu d'évasion en Python qui se joue dans le terminal.

## L'histoire

Tu t'es endormi pendant une intervention de nuit. Quand tu te réveilles, le datacenter est verrouillé. Pour sortir, il faut fouiller les salles, ramasser des objets, ouvrir des portes et résoudre des énigmes avant que l'alarme ne se déclenche. Tu as 15 minutes.

## Lancer le jeu

Il faut Python 3 installé. Depuis le dossier du projet :

```bash
python main.py
```

Sous Windows, si `python` n'est pas reconnu, essaie `py main.py`.

## Les commandes

| Commande | Effet |
|---|---|
| `regarder` | décrit la salle où tu te trouves |
| `aller <direction>` | se déplace (nord, sud, est, ouest) |
| `prendre <objet>` | ramasse un objet de la salle |
| `inventaire` | affiche ce que tu portes |
| `utiliser <objet>` | utilise un objet, par exemple pour ouvrir une porte |
| `temps` | affiche le temps restant |
| `sauver` | sauvegarde la partie |
| `charger` | recharge la dernière sauvegarde |
| `aide` | affiche la liste des commandes |
| `quitter` | quitte le jeu |

## Comment gagner

Trouve la sortie avant la fin du compte à rebours. Certaines portes sont verrouillées, et certaines salles sont protégées par une énigme : il faut y répondre pour entrer, et tu as trois essais.

## Les fichiers du projet

| Fichier | Rôle |
|---|---|
| `main.py` | le point d'entrée : la boucle qui lit tes commandes |
| `moteur.py` | le cœur du jeu : la partie en cours et les commandes |
| `enigmes.py` | les énigmes |
| `salles.json` | la carte : les salles, leurs sorties, leurs objets |
| `.gitignore` | les fichiers que Git ignore (dont `sauvegarde.json`) |

## Agrandir la carte

Pour ajouter une salle, il suffit de la décrire dans `salles.json` et de la relier à une salle existante, dans les deux sens.

## Comment ce projet a été construit

Chaque fonctionnalité et chaque correction a son issue, sa branche et sa pull request. L'historique du dépôt raconte la construction du jeu.
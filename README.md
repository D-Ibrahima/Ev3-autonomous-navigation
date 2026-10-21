# Robot mobile autonome — LEGO Mindstorms EV3

Conception et programmation d'un robot mobile autonome sur plateforme **LEGO Mindstorms EV3**, capable d'explorer un environnement inconnu sans carte préalable. Le robot utilise ses capteurs pour percevoir son environnement et prendre des décisions en temps réel afin de choisir sa trajectoire et poursuivre l'exploration.

Ce projet m'a permis de travailler sur la navigation autonome, la logique de décision et la mise en place de comportements robotiques simples pour gérer les intersections, éviter les impasses et s'adapter à des situations variées. L'accent a été mis sur la fiabilité du comportement et l'intégration cohérente entre capteurs et actionneurs.

**Contexte :** projet réalisé en L2 (deuxième année de licence).

Avec le même robot, j'ai développé plusieurs applications, chacune dans un programme Python du dossier [`robot-ev3-navigation/src`](robot-ev3-navigation/src/).

## Applications

| Programme | Ce qu'il fait | Capteurs utilisés |
|---|---|---|
| [`autodrive_evitement_obstacles.py`](robot-ev3-navigation/src/autodrive_evitement_obstacles.py) | Navigation autonome avec évitement d'obstacles : avance si la voie est libre (> 40 cm), pivote dans une direction aléatoire à l'approche d'un obstacle, recule avec alarme sonore et LED en cas de choc | Ultrason, contact |
| [`suivi_de_ligne.py`](robot-ev3-navigation/src/suivi_de_ligne.py) | Suiveur de ligne noire : avance sur le noir, corrige la trajectoire vers la droite sur le blanc et vers la gauche en zone intermédiaire | Capteur de couleur (lumière réfléchie) |
| [`suivi_ligne_obstacles_rouge.py`](robot-ev3-navigation/src/suivi_ligne_obstacles_rouge.py) | Suivi de ligne combiné à la détection d'obstacles (recul puis virage aléatoire sous 20 cm) et arrêt à la détection de la couleur rouge | Capteur de couleur, ultrason |
| [`suivi_couleur_rouge.py`](robot-ev3-navigation/src/suivi_couleur_rouge.py) | Prototype de suivi d'une couleur : tout droit quand le rouge est détecté, sinon correction de trajectoire | Capteur de couleur |
| [`braitenberg_lumiere.py`](robot-ev3-navigation/src/braitenberg_lumiere.py) | Comportement de type véhicule de Braitenberg : la vitesse de chaque moteur dépend de la lumière ambiante mesurée par un capteur, arrêt au-dessus d'un seuil | 2 capteurs de lumière |
| [`labyrinthe_odometrie.py`](robot-ev3-navigation/src/labyrinthe_odometrie.py) | Exploration d'un labyrinthe à partir de la carte fournie : le trajet est découpé en déplacements et en virages à 90° que le robot exécute par odométrie, à partir de la rotation des roues ([vidéo](https://docs.google.com/videos/d/1STZLHLDUGNXziyZEtEbkyLlgyLmQrvhj_RijTd7NfjA/play)) | Encodeurs des moteurs |
| [`polygones_odometrie.py`](robot-ev3-navigation/src/polygones_odometrie.py) | Tracé d'un polygone régulier (vitesse, nombre de côtés et longueur saisis par l'utilisateur) avec calcul de l'angle de virage | Encodeurs des moteurs |

## Démo vidéo

[Exploration du labyrinthe](https://docs.google.com/videos/d/1STZLHLDUGNXziyZEtEbkyLlgyLmQrvhj_RijTd7NfjA/play) : le robot parcourt le labyrinthe à partir de la carte qui lui a été donnée.

## Matériel

- Brique LEGO Mindstorms EV3 sous **ev3dev**
- 2 grands moteurs (ports B et C, ou A et D pour les programmes d'odométrie)
- Capteurs : ultrason, contact, couleur / lumière, selon l'application
- Interface : LED, haut-parleur, boutons de la brique (arrêt du programme)

## Technologies

- Python 3
- [ev3dev2](https://github.com/ev3dev/ev3dev-lang-python), bibliothèque Python pour EV3

## Lancer un programme

Sur la brique EV3 équipée d'ev3dev :

```bash
python3 robot-ev3-navigation/src/suivi_de_ligne.py
```

Les programmes à boucle continue s'arrêtent en appuyant sur n'importe quel bouton de la brique. Les seuils de lumière (noir, blanc, rouge) sont à ajuster selon l'éclairage.

## Origine du code

`autodrive_evitement_obstacles.py` s'appuie sur une démonstration « autodrive » fournie dans le cadre du cours de robotique mobile en 2ème année de licence).

## Pistes d'amélioration

- Autodrive : sous 20 cm d'un obstacle, aucune action n'est prévue dans la boucle ; ajouter une branche pour reculer ou pivoter.
- Remplacer les virages aléatoires par une stratégie d'exploration avec mémoire (cartographie simple, odométrie) pour gérer intersections et impasses de façon systématique.
- Suivi de ligne : passer à une correction proportionnelle (type PID) au lieu de virages à vitesse fixe.
- Détection du rouge : utiliser le mode couleur du capteur (`ColorSensor`) et vérifier la valeur renvoyée.# Ev3-autonomous-navigation

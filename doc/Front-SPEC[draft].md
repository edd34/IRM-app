# Frontend specification

## Framework
We will use flutter framework for creating the frontend application

We will use flutter activity recognition

Page 1 : Feed : une sorte de flux d'actualité des incidents qui se déroulent à Mayotte.
Page 2 : Carte des incidents
Page 3 : Paramètres
Page 4 : Mon profil
Page 5 : 

Notification Push en cas de danger détecté.

----

# Introduction :
Nous voulons créer une application d'info traffic similaire à Waze mais adapté pour le territoire de Mayotte. Elle pourrait permettre aux internautes d'avoir des informations plus rapidement et plus fiablement que sur I.R.M
Les données de l'applications seront collaboratives et communautaires : les conducteurs signaleront des dangers et tous les utilisateurs recevront une notification push lorsqu'un événement sera signalé.

# Tableau des alertes (à titre indicatif)
|Id|Catégorie|Type|Sous-Type|
|--|-------- | -- | --------|
|0 |Information|Manifestation|Parking fermé|
|1 |Information|Manifestation|Mariage|
|2 |Information|Manifestation|Manzaraka|
|3 |Information|Manifestation|Marche|
|4 |Information|Manifestation|Grève|
|5 |Alerte|Embouteillage|Moyen|
|6 |Alerte|Embouteillage|Intense|
|7 |Information|Signalisation|Feux temporaire|
|8 |Information|Chaussée|Chaussée rétrécie|
|9 |Danger|Agression|Caillassage|
|10|Danger|Chaussée|Arbre sur la chaussée|
|11|Danger|Chaussée|Nid de poule|
|12|Danger|Chaussée|Gravillon|
|13|Danger|Accident|Accident|
|14|Danger|Travaux|Travaux la chaussée|

# Feature list
## Feature 1 : carte des incidents
Description : afficher sur une carte les utilisateurs, ainsi que les incidents signalés sur la route.
Ressources : 
 * [https://usabilitygeek.com/wp-content/uploads/2018/08/ux-case-study-google-maps-waze-home.jpg](https://usabilitygeek.com/wp-content/uploads/2018/08/ux-case-study-google-maps-waze-home.jpg)
 * [Plugin openstreetmap flutter](https://flutterawesome.com/openstreetmap-plugin-for-flutter/)
 * [Leaflet map flutter](https://github.com/fleaflet/flutter_map)

**Remarques** : privilégier les solutions opensource, éviter les solutions qui nécéssitent une clé API car la finalité sera de payer.

## Feature 2 : ajouter un incident
Nous souhaitons que les usagers de la routes puissent rajouter un incident en fonction de la table ci-dessus.
Nous allons avoir un gros bouton sur le côté bas de la carte qui permet de rajouter une alerte rapidement.

[https://www.uisources.com/interaction/5-waze-sendreport](https://www.uisources.com/interaction/5-waze-sendreport)

La position GPS, l'horodatage et l'ID de l'incident sont envoyés au backend.

## Feature 3 : notification push et fonctionnement en tant que service (à venir, nice to have, pas urgent)
C'est une feature qu'il faudra explorer. Nous aurons besoins de cette fonctionnalité pour alerte d'un incident grâce qui nécessite au conducteur de rebrousser chemin.

## Feature 4 : voter pour contribuer à vérifier une information
Nous utiliserons un système de vote pour vérifier les informations et donner un score de fiabilité. Ci-dessous un exemple de tableau avec les items que l'on peut utiliser pour le vote
|Id|Libellé|
|--| -- |
|0 |Oui|
|1 |Peut-être que oui|
|2 |Je ne sais pas|
|3 |Peut-être que non|
|5 |Non|

## Feature 5 (se connecter / s'inscrire)
L'utilisateur doit s'inscrire afin de pouvoir signaler des incidents sur la route ou 

**Feature à venir :** , Feature 6 (Paramètres), Feature 7 (Mon profil)

---

Côté backend j'ai déjà deux routes créées pour récupérer les incidents et ajouter les incidents.
Je travaille surtout sur un système qui permet d'établir un consensus dans des données générées par les utilisateurs ("crowdsourced data")
Pour cela : il faut d'abord récupérer les votes et établir des statistiques pour déterminer la probabilité de véracité de l'information.

Ressources que je lis en ce moment :
 * https://je-suis-tm.github.io/machine-learning/wisdom-of-crowds/
 * https://duckduckgo.com/?t=ffab&q=Dawid-Skene+Model&ia=web
 * https://duckduckgo.com/?q=score+trust+crowdsourced+data+python&t=ffab&ia=web

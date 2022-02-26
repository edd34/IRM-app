# Specification

Specifications principales :
 * alerter les dangers
 * donner des informations sur les embouteillages
 * possibilité de localiser les ambulances et les pompiers pour les permettre de circuler

## Alerter les dangers
Un des objectifs principaux de l'application est d'alerter sur les dangers de la route. Aujourd'hui cela est fait grâce à la radio Mayotte 1ère ou les réseaux sociaux.

Grâce à une application, les données seront disponibles à tout moment via l'application. L'application sera aussi personnalisée et adaptée au contexte de Mayotte.

Types de dangers
 * Route bloquée (barrage, arbre, travaux, mouvement de grève)
 * Travaux
 * Nid de poule
 * Force de l'ordre en intervention
 * embouteillage

Type d'alerte :
 * Notification push sur le smartphone
 * Alerte sonore
 * Vibration du téléphone


## Donner des informations sur les embouteillages


# Technologie à utiliser
## Développement d'application
 * Flutter activity recognition : detect when driving

## Base de donnée NoSQL
Nous utiliserons une base de données NoSQL comme MongoDB car nous ne connaissons pas à l'avance les types de danger que nous allons lister

###
Backend :
django
Django DRF
djoser
django-mongo ?

# API IRM-app

In this file you will find documentation about the IRM API.
The base API URL is http://localhost:8000

## 1. Traffic-Alert component
Data structure :
 * UUID : Unique identifier for each alert in traffic_alert table,
 * lat : latitude of GPS coordinate
 * lon : longitude of GPS coordinate
 * timestamp : timestamp of GPS report
 * localisation : common name of localisation
 * city : name of city
 * municipality : name of municipality
 * report_description : report description


### a. Get all alert

-     GET: /get-traffic-alert/

Description : return a JSON containing all languages in the database
Example : [http://localhost:8000/get-traffic-alert/](http://localhost:8000/get-traffic-alert/)

Example of response :

```json
[
    {
        "UUID": "3970b438-7d79-4319-9600-0575b4c15cce",
        "lat": "45.000000",
        "lon": "12.000000",
        "timestamp": "2022-03-01T10:21:54.630653Z",
        "localisation_description": "mangabandra",
        "report_description": "gene"
    },
]
```

### b. Create a traffic-alert

-     POST: /create-traffic-alert/

Description : return a JSON containing all languages in the database
Example : [http://localhost:8000/create-traffic-alert/](http://localhost:8000/create-traffic-alert/)

Example of body :
```json
{
   "lat" : 45,
   "lon" :12,
   "localisation_description" : "mangabandra",
   "report_description" :"gene"
}
```

Example of response :
```json
{
    "lat": "45.000000",
    "lon": "12.000000",
    "localisation_description": "mangabandra",
    "report_description": "gene"
}
```

## 2. Alert-Table component
Description : this table will categorize types of alert. Front-end will use this table for getting alert type.

**Data structure :**
 * category : category of an alert
 * alert_type : a type of an alert
 * alert_subtype : a subtype of an alert

---
**Example of alert table :**

*Caution : This alert table is not definitive and is provided for information only. *

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
---

### a. Get All Alert in Alert Table
-     GET: /get-alert-table/

Description : return a JSON containing all languages in the database
Example : [http://localhost:8000/get-alert-table/](http://localhost:8000/get-alert-table/)

Example of response :
```json
[
    {
        "id": 1,
        "category": "Information",
        "alert_type": "Manifestation",
        "alert_subtype": "Parking fermé"
    },
    {
        "id": 2,
        "category": "Information",
        "alert_type": "Manifestation",
        "alert_subtype": "Mariage"
    },
    {
        "id": 3,
        "category": "Information",
        "alert_type": "Manifestation",
        "alert_subtype": "Manzaraka"
    },
    {
        "id": 4,
        "category": "Information",
        "alert_type": "Manifestation",
        "alert_subtype": "Marche"
    },
    {
        "id": 5,
        "category": "Information",
        "alert_type": "Manifestation",
        "alert_subtype": "Grève"
    },
    {
        "id": 6,
        "category": "Information",
        "alert_type": "Signalisation",
        "alert_subtype": "Feux temporaire"
    }
]
```

### b. Create an alert type in Alert Table

-     POST: /add-alert-table/

Description : return a JSON containing all languages in the database
Example : [http://localhost:8000/add-alert-table/](http://localhost:8000/add-alert-table/)

Example of json body :
```json
{
    "category":"Information",
    "alert_type":"Signalisation",
    "alert_subtype":"Feux temporaire"
}
```

Example of response :
```json
Status code : 201
{
    "category": "Information",
    "alert_type": "Signalisation",
    "alert_subtype": "Feux temporaire"
}
```

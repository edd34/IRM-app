# API IRM-app

In this file you will find documentation about the IRM API.
The base API URL is http://localhost:8000

## 1. Traffic-Alert component
Data structure :
 * UUID : Unique identifier for each alert in traffic_alert table,
 * lat : latitude of GPS coordinate
 * lon : longitude of GPS coordinate
 * timestamp : timestamp of GPS report
 * localisation_description : common name or description of localisation
 * report_description : report description
 * localisation_id : foreign key in localisation table
 * alert_id : foreign key in alert_table table


### a. Get all alert

-     GET: /get-traffic-alert/

Description : return a JSON containing all languages in the database
Example : [http://localhost:8000/get-traffic-alert/](http://localhost:8000/get-traffic-alert/)

Example of response :

```json
[
    {
        "UUID": "b3ab0f0a-41a4-422f-92ad-9e87a92e4a39",
        "localisation": {
            "id": 1,
            "city": "mangajou",
            "municipality": "sada",
            "postalcode": "97640"
        },
        "alert": {
            "id": 1,
            "category": "Information",
            "alert_type": "Signalisation",
            "alert_subtype": "Feux temporaire"
        },
        "lat": "45.000000",
        "lon": "12.000000",
        "timestamp": "2022-03-05T01:15:07.576589Z",
        "localisation_description": "mangabandra",
        "report_description": "gene",
        "localisation_id": 1,
        "alert_id": 1
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
   "report_description" :"gene",
    "localisation_id": 2,
    "alert_id": 1
}
```

Example of response :
```json
{
    "UUID": "924811c9-db2d-456d-aed1-928d55e00daf",
    "localisation": {
        "id": 2,
        "city": "sada",
        "municipality": "sada",
        "postalcode": "97640"
    },
    "alert": {
        "id": 1,
        "category": "Information",
        "alert_type": "Signalisation",
        "alert_subtype": "Feux temporaire"
    },
    "lat": "45.000000",
    "lon": "12.000000",
    "timestamp": "2022-03-05T09:41:23.577213Z",
    "localisation_description": "si si",
    "report_description": "desc",
    "localisation_id": 2,
    "alert_id": 1
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

## 3. Localisation component
Description : this table will hold information about city, municipality and postal code.

**Data structure :**
 * city : represent the city ("village")
 * municipality : represend the municipality ("commune")
 * postalcode : represent postalcode ("code postal")

---
**Example of localisation table :**

*Caution : This alert table is not definitive and is provided for information only. *

|Id|city|municipality|postalcode|
|--|-------- | -- | --------|
|0 |sada|sada|97640|
|1 |mangajou|sada|97640|
---

### a. Get All Localisations
-     GET: /get-localisations/

Description : return a JSON containing all languages in the database
Example : [http://localhost:8000/get-localisations/](http://localhost:8000/get-localisations/)

Example of response :
```json
[
    {
        "id": 1,
        "city": "mangajou",
        "municipality": "sada",
        "postalcode": "97640"
    },
    {
        "id": 2,
        "city": "sada",
        "municipality": "sada",
        "postalcode": "97640"
    }
]
```

### b. Add a Localisation

-     POST: /add-alert-table/

Description : return a JSON containing all languages in the database
Example : [127.0.0.1:8000/add-localisation/](127.0.0.1:8000/add-localisation/)

Example of json body :
```json
{
    "city" : "chiconi",
    "municipality" : "chiconi",
    "postalcode" : "97640"
}
```

Example of response :
```json
{
    "id": 3,
    "city": "chiconi",
    "municipality": "chiconi",
    "postalcode": "97640"
}
```

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


### a. Get all languages

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
        "localisation": "mangabandra",
        "city": "sada",
        "municipality": "sada",
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
body :
{
   "lat" : 45,
   "lon" :12,
   "localisation" : "mangabandra",
   "city" : "sada",
   "municipality" : "sada",
   "report_description" :"gene"
}
```

Example of response :
```json
Status code : 201
{
    "lat": "45.000000",
    "lon": "12.000000",
    "localisation": "mangabandra",
    "city": "sada",
    "municipality": "sada",
    "report_description": "gene"
}
```
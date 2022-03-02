# IRM-app

Il s'agit du backend d'une application d'info traffic pour le territoire de Mayotte. Il sera possible de géolocaliser un danger sur la route : caillassage, tronc d'arbre, nid de poule, dos d'âne etc... et de partager cette information à tous les usager de la route.


## Configure the virtual environment

### Create a new environment virtualenv

Create a virutal environment using [virtualenv](https://docs.python.org/fr/3/library/venv.html).

```bash
python3 -m venv venv
```

### Entering the environment

```bash
source venv/bin/activate
```

## Installation of package listed in requirement.txt

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip3 install -r requirements.txt
```

## Configure environment variables

1. Rename the file .env-example to .env
2. Fill the variable in .env file

```
POSTGRES_DB=(database name)
POSTGRES_USER=(database username)
POSTGRES_PASSWORD=(database password)
SECRET=(secret key for django operation)
CORS_WHITELIST_DOMAIN=(is the host name of the frontend app)
DJANGO_ENV= (can be dev or prod)
```

## Steps when running the program for the first time.

In order to run the backend program, you should follow the steps described below. All commands are run from the root folder.

### Refreshing migrations

```bash
python manage.py makemigrations
```

### Applying migrations

```bash
python manage.py migrate
```

### Import a sample database from CSV (TODO)

```bash
python manage.py importdb
```

## Run the program

After the database is populated and correctly setup, you can run the backend server by executing the following command :

```bash
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### API doc

The documentation of the public API is available under doc folder : [API.md](doc/API.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)

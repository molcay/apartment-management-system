# apartment-management-system

This repository contains source code for **apartment-management-system** project.

---

## Development Setup

#### Backend Setup

* Clone this repository and change directory to it.
```bash
git clone git@github.com:molcay/apartment-management-system.git
cd apartment-management-system
```

* Create virtual environment and activate it (consider using `pipenv`).
```bash
pipenv shell  # this command activate virtual environment. If the environment did not exist, first it creates and activate.
```

* Install dependencies (please use `Pipfile`).
```bash
pipenv install
```

* Ensure that the database configured correctly.
> defaults: DB_NAME=`ams_db`, USER=`admin`, PASSWORD=`admin`, host=`localhost`, PORT=`5432` 

* Start application.
```bash
python manage.py runserver
```

* If you want to populated database, then use:
```bash
python manage.py shell < scripts/seed.py
```

#### Frontend Setup

* Change directory to `frontend`:
```bash
cd frontend
```

* Install dependency:
```bash
yarn install
```

* Run webpack server:
```bash
yarn dev
```

> NOTE: If you want to develop front-end you need to start backend as well.

#### Docker for `PostgreSQL`
* Run `postgresql` as docker container 
```bash
docker run -p 5432:5432 --name ams-postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -d postgres
```
> Please not that the data of the database is volatile.

* Start docker container with:
```bash
docker start ams-postgres
```

* Stop docker container with:
```bash
docker stop ams-postgres
```

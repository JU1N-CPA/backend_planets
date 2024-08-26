# Django REST Framework Planets API

This project is a Django REST framework application for managing planetary data. It interacts with a GraphQL API to fetch, create, update, and delete records of planets.

## My thoughts
This test doesn't include to many best practices I would like to implemet, however, all the requirements for the test were implemented. time invested: 2h.

At the same time, I'm working in a new version that you can discover more best practices such as:
- insert error handlers to the views
- double records added handler
- Improve serializers
- split the views, serializer,views in different folders
- create docker for easy deploy
- implementation of nginx for proxy configurations
- implementation of jwt for proctected views
- API documentation Swagger
- Unit tests

You can see the following repo where these implementations can be found. However, it can be in done in the next days.

## Installation and Setup

### 0. Clone repository
git clone https://github.com/JU1N-CPA/backend_planets.git

### 1. Install Python

Ensure Python is installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/).

### 2. Create a Virtual Environment

Create and activate a virtual environment to manage project dependencies:

```
python -m venv env
```

#### 2.1. Create a Virtual Environment
Activate the virtual environment:
On Windows:
```
.\env\Scripts\activate
```
On macOS/Linux:
```
source env/bin/activate
```

### 3. Install dependencies
Install requirements.txt

```
pip install -r requirements.txt
```

### 4. Run Migrations
Navigate to your project directory and run the migrations to set up the database schema:

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Open and Interact with the SQLite Database
To open and interact with the SQLite database, use the following command:
```
sqlite3 /home/juanlinux/repos/persnalProjects/back-basic-planets/core/db.sqlite3
```
Commands to Use in SQLite

List Tables:

```
.tables
```

Run Queries:
You can run SQL queries to view or modify the data. For example:

```
SELECT * FROM planets_planet;
```

Exit SQLite:

```
.quit
```

## API Endpoints

### 1. Create a New Record
Send a POST request to create a new planet record. Example using curl:

```
curl -X POST http://localhost:8000/api/planets/create/ -H "Content-Type: application/json" -d '{"name": "New Planet", "population": 123456, "terrains": "forest-mountain", "climates": "temperate"}'
```

### 2. Update a Record
Send a PUT request to update an existing planet record. Example using curl:

```
curl -X PUT http://localhost:8000/api/planets/<str:name>/ -H "Content-Type: application/json" -d '{"population": 654321, "terrains": "desert", "climates": "arid"}'
```

Replace <str:name> with the name of the planet you want to update.


### 3. Delete a Record
Send a DELETE request to delete a planet record by name. Example using curl:

```
curl -X DELETE http://localhost:8000/api/planets/delete/<str:name>/
```

Replace <str:name> with the name of the planet you want to delete.

## Running the Development Server
To run the Django development server, use the following command:

```
python manage.py runserver
```
You can then access the API at http://localhost:8000/.

## Summary
Install Python
Create and activate a virtual environment
Install Django and Django REST framework
Run migrations to set up the database
Interact with the SQLite database using sqlite3
Create, update, and delete records using API endpoints
For more information, refer to the Django documentation and Django REST framework documentation.

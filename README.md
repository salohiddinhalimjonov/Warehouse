# Warehouse

## Project Setup
### Create Virtual Environment
```virtualenv venv```

### Activate Virtual Environment
```source venv/bin/activate```

### Configure Environment files
```cp .env.example .env```

edit .env file and add your own credentials

### Install Dependencies
```pip install -r requirements.txt```

### Upload initial data
```
python manage.py migrate
python load_data.py  
```
For loading the data, run python script above or connect to the project database and run 
sql commands in warehouse.sql file

### Run project
```
python manage.py runserver
```

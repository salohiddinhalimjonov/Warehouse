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
For loading the data, run python script below ( python load_data.py ) or connect to the project database and run 
sql commands in warehouse.sql file
```
python manage.py migrate
python load_data.py  
```

### Run project
```
python manage.py runserver
```

### Run API
```
http://127.0.0.1:8000/api/v1/warehouse/statistics/
```

### Expected Result

![result](https://github.com/salohiddinhalimjonov/Warehouse/assets/72136403/49d24726-49da-4b6d-8137-5ef6c056dca1)

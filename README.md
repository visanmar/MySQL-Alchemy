# Tasks list using Flask, SQLAlchemy and MySQL in Python. VUE frontend.
Working example using Python Flask with SQLAlchemy, MySQL and VUE frontend.

## What does this project use?
- Python
- Python dotenv
- Flask
- Flask SQLAlchemy
- Flask CORS
- MySQL Connector
- VUE
- VUE SweetAlert 2
- VUE toastification


## Requirements,  initialization and start it


### Python virtual environment
Inside app root directory (where you clone this repository):
```cmd
pip install virtualenv
python -m virtualenv -p python3 env
.\env\Scripts\activate
```

### Dependencies
```cmd
pip install python-dotenv
pip install flask
pip install flask-sqlalchemy
pip install flask_cors
pip install flask-marshmallow
pip install marshmallow-sqlalchemy
pip install mysql-connector
```

### Before run
- Modify the dot env ('.env') file in app root directory (where you clone this repository) and set the MySQL connection URI:
  ```cmd
  SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://[MySQL server]:3306/[database]
  ```
- Go to VUE app frontend and download dependencies:
  ```cmd
  cd alchemy-vue
  npm install -E
  ```

### Run the proyect
Make sure your MySQL server is running.

Inside app root directory (where you clone this repository):
- Run Python app:
  ```cmd
  python ./src/app.py
  ```
- Run VUE frontend app:
  ```cmd
  cd alchemy-vue
  npm run server
  ```
- In web browser go to (usually): [http://localhost:8080/](http://localhost:8080/)


# how to setup the project

## 1 - install backend requirements
- install python in your PC

- create virtual envirement ->
python -m venv venv

- activate it -> 
venv\Scripts\activate

- install packages -> 
pip install -r backend\requirments.txt

- add table to database ->
python manage.py makemigrations <->
python manage.py migrate

- run the backend server ->
python manage.py runserver

## 2 - install frontend requirements
- install node in your PC

- install frontend packages ->
cd frontend <->
npm install 

- run the frontend server ->
npm run serve

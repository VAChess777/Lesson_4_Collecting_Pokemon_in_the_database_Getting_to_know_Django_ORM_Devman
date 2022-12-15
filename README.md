# The Pokemon map

A program for creating a Pokemon card. Allows the user to display information about any Pokemon and its current location in a convenient form.

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)


### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777/Lesson_4_Collecting_Pokemon_in_the_database_Getting_to_know_Django_ORM_Devman](https://github.com/VAChess777/Lesson_4_Collecting_Pokemon_in_the_database_Getting_to_know_Django_ORM_Devman), or clone the `git` repository to a local folder:
```
https://github.com/VAChess777/Lesson_4_Collecting_Pokemon_in_the_database_Getting_to_know_Django_ORM_Devman
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### About environment variables:

The program `settings.py ` there are environment variables in the `project` folder that are responsible for configuring access to the database.
create a `.env` file, place it in the root directory of the program. Put the following data in the `.env` file in the `key=value` format.

`DB_NAME=` - Database name. 
`SECRET_KEY=` - Django secret key.              
`DEBUG=` - True for enabling debugging mode, False for production. The default value is `False`.                                                         
`ALLOWED_HOSTS=` - This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.
Example of ALLOWED_HOSTS settings in file. env - `ALLOWED_HOSTS = ['www.djangoproject.dev', 'docs.djangoproject.dev', 'localhost' ...]`. Where
`www.djangoproject.dev', 'docs.djangoproject.dev, 'localhost'` -  addresses of allowed hosts. The default value is `localhost`.   

### How to run the program:

* Run the migration of models and database creation with the following commands in the console:
```angular2html
python manage.py makemigrations
```
```angular2html
python manage.py migrate
```
* After that, you can start the local server:
```angular2html
python manage.py runserver
```
![](https://github.com/VAChess777/images_/blob/1d7788c28592fca3aeb55d39eee588de68ea41d5/Empty_map_of_Moscow.png)

* Then we create the administrative part of the site.
```angular2html
python manage.py createsuperuser
```
Pokemon and their location on the map is more convenient to add through it.

* Starting the server again:
```angular2html
python manage.py runserver
```
* Go to the admin panel http://127.0.0.1:8000/admin/                             
![](https://github.com/VAChess777/images_/blob/1d7788c28592fca3aeb55d39eee588de68ea41d5/Login_to_Django_admin_panel.png)

The site admin panel looks like this:

![](https://github.com/VAChess777/images_/blob/1d7788c28592fca3aeb55d39eee588de68ea41d5/Django_Admin_panel.png)





























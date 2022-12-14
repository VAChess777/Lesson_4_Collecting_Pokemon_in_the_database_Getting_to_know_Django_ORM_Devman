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
Pokemon and their location on the map is more convenient to add through it.
```angular2html
python manage.py createsuperuser
```


* Starting the server again:
```angular2html
python manage.py runserver
```
* Go to the admin panel http://127.0.0.1:8000/admin/  

![](https://github.com/VAChess777/images_/blob/3f7e679d5e61982a2a879946221642e0e2926851/Django_Admin_panel_1.png)

The site admin panel looks like this:

![](https://github.com/VAChess777/images_/blob/1d7788c28592fca3aeb55d39eee588de68ea41d5/Django_Admin_panel.png)


* Using the Pokemon menu section, you can add Pokemon models

* Using the Pokemon entitys section, you can add a model to describe the appearances/disappearances of Pokemon, as well as additional options

* After entering data on all manifestations, Pokemon will appear on the map:

* If you have not launched the site on the local server, then run it with the command in the console:
```angular2html
python manage.py runserver
```
### How the program works:

The program contains scripts:

```manage.py``` - the program that runs the server.           
```settings.py``` - the program is located in the project folder. Responsible for setting up access to the site database.   
```models.py``` - the program is located in the datacenter folder. The program is responsible for data models and their fields.          
```urls.py``` - the program is located in the project folder. Responsible for setting up links to site pages.           
```views.py``` - the program responsible for displaying Pokemon on the map.

### Features works of the program:

The `views.py` program contains the functions:

* The `add_pokemon` function - adds Pokemon to the map.
* The `show_all_pokemons` function - responsible for displaying all Pokemon on the main page map.
* The `show_pokemon` function - responsible for displaying Pokemon and its evolution on the pokemon page itself.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).

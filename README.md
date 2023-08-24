# It company task manager

## Check it Out

[Task Manager deployed to render](https://task-manager-n7we.onrender.com)
- Login: ```TestWorker```
- Password: ```testpass123```
## Table of Contents
 1. [Introduction](#introduction)
 2. [Requirements](#requirements)
 3. [Installation](#installation)
 4. [Used technogies](#used-technologies)
 5. [Usage](#usage)
 6. [UML](#uml)


## Introduction
It company task manager is provided for helping
workers and managers in IT industry to manage and control
their task flow

## Requirements
* python 3.8
* pip

## Installation
1. Clone this repository:
    ```https://github.com/Kirontiko/it-company-task-manager.git```
2. Create virtual environment and activate it:
   * Tooltip for windows:
     - ```python -m venv venv``` 
     - ```venv\Scripts\activate```
   * Tooltip for mac:
     - ```python -m venv venv```
     - ```source venv/bin/activate```

3. Install dependencies:
    - ```pip install -r requirements.txt```

4. Apply all migrations in database:
   - ```python manage.py migrate```

5. Create superuser and apply Login and Password
   (You can skip email)
   - ```python manage.py createsuperuser```
6. You can load prepared data for database using this command:
   - ```python manage.py loaddata it_task_manager_example_data.json```

7. Start running django server using this command:
   - ```python manage.py runserver```
   - You will see something like this:
   ```
     Watching for file changes with StatReloader
     System check identified no issues (0 silenced).
     July 25, 2023 - 11:54:15
     Django version 4.1, using settings 'config.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.```
8. Click at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your terminal 
   and you will see Login page. Pass your login and password,
   which you`ve used while creating superuser and you will 
   access to the home page

## Used technologies
- Django framework
- HTML, CSS
- SQLite
- PostgreSQL

## Usage
1. Creating accounts for new workers
2. Creating new task types
3. Creating new tasks and adding them to list
4. Assigning worker to the task or deleting from it
5. Creating new positions for workers
6. Changing deadlines for tasks and status bar(Completed or In process)

## UML
![image](https://github.com/Kirontiko/it-company-task-manager/assets/90575903/deb50426-0d98-496a-9ce2-e494d5e15dad)

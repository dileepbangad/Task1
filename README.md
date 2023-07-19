# Task1
In this project, we are implementing the business logic for a simplified elevator model in Python.All we are going to do is to decide whether the elevator should go up, go down, or stop. 
It is implemented using Python & Django (Django Rest Framework specifically with Models, ViewSets, Serializers etc)
An elevator system, which can be initialised with N elevators and maintains the elevator states as well.
Programming Language - Python
Framework - Django
Database - PostgreSQL
No. of Tables in Database – 2
Table 1 : Elevators
    Attributes - name, current_floor, max_floor, is_operational 
Table 2 : Elevator Requests 
    Attributes - request_floor, request_time, elevator

No. of APIs Created – 6
1. Initialise the elevator system to create ‘n’ elevators in the system - http://localhost:8000/addelevator
    request Body = {'name':'elevator1','max_floor':5}
    API Response - It create new Elevator in elevators tabel with unique elevator id.

2. create a request by the user for the elevator - http://localhost:8000/requestelevator
    request Body = {'elevator':1, 'request_floor':5}
    API Response - It create new Request in Elevator Request Table

3. Fetch all requests for a given elevator and Saves user request to the list of requests for a elevator - http://localhost:8000/fetchelevatorrequests
    request Body = {'elevator_id':1}
    API Response - It shows all the request for the elevator Id and also give the list of request for a elevator

4. Fetch the next destination floor for a given elevator and Fetch if the elevator is moving up or down currently - http://localhost:8000/fetchnextdestrequests
    request Body = {'elevator_id':1}
    API Response - It shows the current_floor, destination_floor, and the direction of lift up or Down

5. Mark a elevator as not working or in maintenance and vice-versa to continue also - http://localhost:8000/markisoperatable
    request Body = {'elevator_id':1}
    API Response - It disable the Elevator mark is_operational = False in the Elevator table in Database and the same API if we call again it will again mark is_operational = True it implies elevator is in working condition.

6. Open/close the door, and also show the current-floor and next upcoming floor - http://localhost:8000/openclose
    request Body = {'elevator_id':1}
    API Response - It move up from the current_floor -> dest_floor and now show current_floor and the next upcoming floor.

All the necessary requirements according to the task description is fullfeed. All functionalities and features are implemented in each APIs according to the requirements.

Instructions on how to run code -
First you should change the database connectivity from settings.py file with your database
connection and then write these commands -
1. Pip install Django
2. Pip install Psycopg2
3. Pip install djangorestframework
4. Python manage.py makemigrations
5. Python manage.py migrate
6. Python manage.py runserver
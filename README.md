# Game of Live

<h3>Run project in the Docker</h3>
1 --- Run building client and server --- <br>
  - Run <b>build-dev-server.sh</b> to build server and client.
<br>
2 --- Start server and client --- <br>
  - Run <b>run-dev-server.sh</b> every time you want to start server.
<br>
Client run http://0.0.0.0:8080/ 

Server run http://0.0.0.0:7000/
<br>
<h3>Django migrations</h3>
1 --- If you want to create new migrations based on model changes --- <br>
 - Run <b>docker-compose exec server python manage.py makemigrations</b>
<br>
2 --- If you want to apply current migrations --- <br>
 - Run <b>docker-compose exec server python manage.py migrate</b>

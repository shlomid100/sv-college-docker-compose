# sv-college-docker-compose with mysql

1. created python file app.py to create web portal with below method to display "Hello World"
   @app.route("/") 
   def hello(): 
     return "Hello World!"
     
   the app listen on port 3000 and do connection to the MYSQL DB in method: connect_to_mysql, with app.py we have two files .env to set all environment vars, in order to use it in the app.py NEED to add lines:
   import os 
   from dotenv import load_dotenv
   
   and after the import, code call: load_dotenv(), and then we can use the .env file like in app.py: user=os.getenv("MYSQL_USERNAME") see in app.py
   
2. Create Dockerfile to build image base on python to run the above app.py with copy of requirements.txt to install required software versions , see Dockerfile

3. Create image from the Dockerfile : docker build -t python-app:0.1 . --> to use it in the dockercompose to create container from it

4. Created docker-compose.yaml which start two services python app and mysql server, I added dependency of healthcheck saw python app will not try connect to mysql till it's up, as i got error 
   since it try connect to mysql before it was ready, see docker-compose.yaml.
   
5. After the two conatiners are up, I connected to the mysql server: docker exec -it mysqldb bash, then connect to sql prompt by: mysql -h localhost -uroot -pS...! , Insid we can see the databases:
   show databases; --> then choose a db:  use mysql; --> see the tables in db: show tables; --> then run sql on it: select * from user;

6. In oreder to look on the DB with client I used dbevear/cloudbeaver added to compose.yaml the service cloudbeaver also add it the health check so will be  
   available only after mysql service is up
    after MYSQL is u, after it's up do: docker exec -it cloudbeaver bash and see the volume inside: /opt/cloudbeaver/workspace

7. open the UI of cloudbeaver http://localhost:8080/ define the admin details cbadmin/Sd..! and create connection to our MYSQL DB, need to set the service IP not localhost
 

# sv-college-docker-compose
DB --> MONGODB
ClientDB = Mongo Compass
express in Jnods it's like Flask in python
mongoose - library for mongodb connection

create image with MongoDB
# sv-college-docker-compose
DB --> MONGODB
ClientDB = Mongo Compass
express in Jnods it's like Flask in python

Create SQL Database MySQL Using Docker Compose
Create Python Web Application
Create Connection To MySQL Using Environment Variable + Volume
Create New Dockerfile
Build Your Image Using Tag python_mysql:v0.1
Test Locally The Application VIA Docker Compose (Using Port 3000)
Uplaod Your Docker Compose File To Git
Extra: MySQL Client for UI


MONGODB - 


Client - Mongo-Compass
Server - MongoDB

Basic URI = mongodb://localhost:27017

express - web framewokr for nodejs
mongoose - library for mongodb conection

docker volume create sv_mongo_data

docker run -d \
--name mongodb \
-p 27018:27017 \
-e MONGO_INITDB_ROOT_USERNAME=root \
-e MONGO_INITDB_ROOT_PASSWORD=secretPassword \
-v sv_mongo_data:/data/db \
mongo:latest

mongo CLI (docker)
mongo Client (docker compass)
mongo SDK (javascript)

dotenv

docker build -t node-app:0.1 .

docker run -d --name node-app -p 3005:3005 node-app:0.1


docker run -d --name node-app -e MONGO_PORT=27017 -e MONGO_HOST=172.17.0.2 -p 3005:3005 node-app:0.1

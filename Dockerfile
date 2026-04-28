FROM node:18

WORKDIR /app

COPY package*.json . 
# requirements.txt for python, pom.xml for java, etc.

RUN npm install

COPY . .

EXPOSE 3005

CMD [ "node", "index.js" ]

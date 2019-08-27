# FROM node:10-alpine
FROM node:carbon

ENV FOO hello_world

# Create app directory
WORKDIR /app

# Install nodemon for hot reload
RUN npm install -g nodemon

# Install app dependencies
COPY package*.json ./

RUN npm install

# Bundle app source
# COPY . .
COPY src /app

EXPOSE 8080

CMD [ "nodemon", "/app/src/server.js" ]
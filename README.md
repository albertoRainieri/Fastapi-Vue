# Overview
FastApi Application with Mysql, PhpMyAdmin

# Setup
Fill in the .env file

# Install
Create and Running
```
$ docker-compose up -d --build
```

# MySql configuration
Enter MySql container. Enter mysql console and create a new user
```
$ CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
# CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
$ GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
# GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'%';
$ FLUSH PRIVILEGES;
```

# Alembic
```
Enter backend container and run:

$ alembic revision --autogenerate -m "First Migration";
$ alembic upgrade head;

Reset Containers if something goes wrong.
```

## Frontend
http://localhost
Try this markdown:

![alt text](https://github.com/albertoRainieri/FullStack-Application-Fastapi-Vue.js/blob/main/images/Dashboard.png)

## Check Api Specifications
http://localhost:5000/docs

![alt text](https://github.com/albertoRainieri/FullStack-Application-Fastapi-Vue.js/blob/main/images/Backend.png)


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
// CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
$ GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
// GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'%';
$ FLUSH PRIVILEGES;
```

## Frontend
http://localhost

## Check Api Specifications
http://localhost:5000/docs


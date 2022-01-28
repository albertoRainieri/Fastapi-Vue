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
## issues

frontend container might run into issues. DevDependencies might not be found because they are not installed globally. This may happen if you tried to create the containers many times. In this case, just remove old images/containers and rebuild the frontend image.
If this does not work, you can also fix the issue by running $ npm audit fix inside the container. In order to do that, you need to slightly modify the CMD command in the Dockerfile with "CMD [ "http-server", "./dist" ]", otherwise you can not access the container.

Other issues can be related to alembic (migration tool). Alembic is installed in the backend container. In case something goes wrong, remove tables if present in the mysql (you can use Phpmyadmin for this) and remove alembic/ and alembic.ini in the backend container. Restart alembic by doing "alembic init alembic" and configure "sqlalchemy.url" and "metadata" in the alembic/env.py file. Find more information here "https://alembic.sqlalchemy.org/en/latest/autogenerate.html"
Hope this helps.


## Frontend
http://localhost
Try this markdown:

![alt text](https://github.com/albertoRainieri/FullStack-Application-Fastapi-Vue.js/blob/main/images/Dashboard.png)

## Check Api Specifications
http://localhost:5000/docs

![alt text](https://github.com/albertoRainieri/FullStack-Application-Fastapi-Vue.js/blob/main/images/Backend.png)


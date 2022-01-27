
FROM node:lts-alpine

# make the 'app' folder the current working directory
WORKDIR /app
RUN npm install http-server -g
# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY ./ ./


# build app for production with minification
RUN npm run build
RUN npm audit fix
EXPOSE 80
#CMD [ "http-server", "./dist" ]
CMD ["npm", "run", "serve"]
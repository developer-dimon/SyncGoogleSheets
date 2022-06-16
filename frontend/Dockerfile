FROM node:14.19.3

WORKDIR /home/SyncGoogleSheets/frontend/

COPY ./package.json .
COPY ./package-lock.json .

RUN npm install

COPY . .

RUN npm run build


FROM node:14

WORKDIR /ass6ujjwal

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "start"]

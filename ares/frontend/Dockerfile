FROM node:16-alpine

ENV URL=http://0.0.0.0:5000/api

WORKDIR /app

ADD . .

RUN npm install

ENTRYPOINT ["node"]

CMD ["app.js"]
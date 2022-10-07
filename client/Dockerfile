FROM node:16

COPY ./package.json /home/node/app/
WORKDIR /home/node/app

COPY --chown=node:node . /home/node/app
RUN npm install -g npm && npm install

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh

RUN chown -R node /home/node/app/node_modules

ENV HOST 0.0.0.0
EXPOSE 3000

USER node

ENTRYPOINT [ "entrypoint.sh" ]
CMD npm run start
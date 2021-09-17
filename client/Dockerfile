FROM node:lts-alpine AS development

RUN apk update && \
    apk add git
WORKDIR /front
COPY . .

FROM node:lts-alpine AS builder

# Create app directory
WORKDIR /app
ADD . /app/

# global install & update
RUN npm i -g npm && npm i -g yarn

RUN rm yarn.lock
RUN yarn
RUN yarn build

ENV HOST 0.0.0.0
EXPOSE 3000

# start command
CMD [ "yarn", "start" ]
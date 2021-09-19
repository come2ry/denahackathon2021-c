FROM node:lts-alpine AS development

RUN apk update && \
    apk add git
WORKDIR /front
COPY . .

FROM node:lts-alpine AS builder

WORKDIR /client
ADD . /client/

ARG NUXT_APP_BACK_HOST
ENV NUXT_APP_BACK_HOST ${NUXT_APP_BACK_HOST}
RUN rm yarn.lock
RUN yarn
RUN yarn build

ENV HOST 0.0.0.0
EXPOSE 3000

# start command
CMD [ "yarn", "start" ]
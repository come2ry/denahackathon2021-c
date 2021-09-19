build:
	docker-compose build

upd:
	docker-compose up -d
upd-back:
	docker-compose up db server swagger-ui

up:
	docker-compose up
up-back:
	docker-compose up db server swagger-ui

down:
	docker-compose down

ps:
	docker-compose ps

images:
	docker-compose images

top:
	docker-compose top

logs:
	docker-compose logs -f
logs-client:
	docker-compose logs -f client
logs-server:
	docker-compose logs -f server

login-client:
	docker-compose exec client /bin/bash
login-server:
	docker-compose exec server /bin/bash

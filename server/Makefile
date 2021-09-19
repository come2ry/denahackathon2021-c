test:
	pytest -s .

db-init:
	flask createdb

migrate:
	alembic --config alembic.ini revision --autogenerate -m "$(m)"

upgrade:
	alembic --config alembic.ini upgrade head
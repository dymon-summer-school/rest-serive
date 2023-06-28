# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up-prod test

down:
	docker compose down

build: down
	docker compose build

up: build
	docker compose up

# no logs
up-prod: build
	docker compose up -d

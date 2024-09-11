# test
hello:
	echo "Hello World!"

down:
	docker compose down

down-hard:
	docker compose down -v

dev:
	docker compose up --build

dev-watch:
	docker compose up --build --watch

test:
	docker compose -f ./compose.test.yml up --build
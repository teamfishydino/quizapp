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

# test:
# 	docker compose -f ./compose.test.yml run --build --rm api pytest -x

test:
	docker compose -f ./compose.test.yml run --build --service-ports --rm api
	docker compose down

workflow-test:
	docker compose -f ./compose.test.yml run --build --service-ports -e MONGO_URI -e MONGO_TEST_URI api
	docker compose down
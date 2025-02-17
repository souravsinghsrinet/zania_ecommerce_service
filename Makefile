IMAGE_NAME = small_ecommerce_api:v1
CONTAINER_NAME = small_ecommerce_api

TEST_IMAGE_NAME = test_small_ecommerce_api:v1
TEST_CONTAINER_NAME = test_small_ecommerce_api

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --env-file=app.env -p 8000:8080 --name $(CONTAINER_NAME) $(IMAGE_NAME)

remove:
	docker rm $(CONTAINER_NAME)

rebuild:
	make build
	make remove
	make run

buildtest:
	docker build -t $(TEST_IMAGE_NAME) -f Dockerfile.test .

runtest:
	docker run --env-file=app.env --name $(TEST_CONTAINER_NAME) $(TEST_IMAGE_NAME)

removetest:
	docker rm $(TEST_CONTAINER_NAME)

rebuildtest:
	make buildtest
	make removetest
	make runtest
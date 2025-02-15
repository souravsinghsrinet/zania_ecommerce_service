IMAGE_NAME = small_ecommerce_api:v1
CONTAINER_NAME = small_ecommerce_api

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 8000:8080 --name $(CONTAINER_NAME) $(IMAGE_NAME)

remove:
	docker rm $(CONTAINER_NAME)

rebuild:
	make build
	make remove
	make run

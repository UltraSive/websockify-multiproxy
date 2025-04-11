# Makefile

# Name of the Docker image
IMAGE_NAME := websockify-multiproxy

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# test the Docker container
test:
	docker run --name vnc-websocket-multiproxy --network host $(IMAGE_NAME)

# Run the Docker container
run:
	docker run -d --name vnc-websocket-multiproxy --network host $(IMAGE_NAME)

# Stop and remove the container
stop:
	docker stop vnc-websocket-multiproxy && docker rm vnc-websocket-multiproxy

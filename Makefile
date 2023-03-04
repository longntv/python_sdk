# Define the Python interpreter to use.
PYTHON=python3

# Define the name of the virtual environment.
VENV_NAME=.venv

# Define the name of the requirements file.
REQUIREMENTS=requirements.txt

# Define the name of the entrypoint file.
ENTRYPOINT=main.py

# Define the name of the Docker image.
DOCKER_IMAGE=myapp

# Define the name of the Docker container.
DOCKER_CONTAINER=myapp

# Install the dependencies.
install:
	$(PYTHON) -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip install -r $(REQUIREMENTS)

# Run the application.
run:
	$(PYTHON) $(ENTRYPOINT)

# Build the Docker image.
docker-build:
	docker build -t $(DOCKER_IMAGE) .

# Run the Docker container.
docker-run:
	docker run --rm --name $(DOCKER_CONTAINER) -p 5000:5000 $(DOCKER_IMAGE)

# Stop the Docker container.
docker-stop:
	docker stop $(DOCKER_CONTAINER)

# Remove the virtual environment.
clean:
	rm -rf $(VENV_NAME)
	$(PYTHON) -m pyclean .

.PHONY: install run docker-build docker-run docker-stop clean

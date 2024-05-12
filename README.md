# Dockerized FastAPI Application

This repository contains a Dockerized FastAPI application for serving machine learning models. The application provides endpoints for making predictions on input images using pre-trained models.

## Getting Started

To get started with using this Dockerized FastAPI application, follow these steps:

### Prerequisites

- Docker installed on your machine. You can download and install Docker from [here](https://docs.docker.com/get-docker/).

### Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the cloned repository directory:

    ```bash
    cd your-repository
    ```

3. Build the Docker image:

    ```bash
    docker build -t fastapi-app .
    ```

4. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 fastapi-app
    ```

5. Access the FastAPI application:

    Open your web browser and go to `http://localhost:8000` to access the FastAPI application.

## Endpoints

The FastAPI application provides the following endpoints:

- `/predict_cervF`: Endpoint for predicting cervical fractures.
- `/predict_boneF`: Endpoint for predicting bone fractures.

Each endpoint expects a POST request with an image file as input. See the API documentation for more details.

## API Documentation

You can access the Swagger UI documentation for the FastAPI application by visiting `http://localhost:8000/docs` in your web browser.

## Questions or Issues

If you have any questions or encounter any issues while using this Dockerized FastAPI application, please [open an issue](https://github.com/your-username/your-repository/issues) on GitHub.


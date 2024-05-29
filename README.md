# Grammar Checker Backend with FastAPI and OpenAI GPT-3.5 Turbo


![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0%2B-green)
![OpenAI](https://img.shields.io/badge/OpenAI-1.30.4%2B-yellow)
![Pydantic](https://img.shields.io/badge/Pydantic-1.10.13%2B-brightgreen)
![Docker](https://img.shields.io/badge/Docker-24.0%2B-blue)

## Introduction

This project aims to develop a backend for a grammar checker using FastAPI as the backend framework and OpenAI's GPT-3.5 Turbo as the Language Model (LLM). The backend provides an API endpoint where text can be uploaded, processed using the LLM, and returns a list of errors found in the text along with their corrections and the type of error.

## Setup and Running the Code

1. **Clone the Repository**: 
   ```
   git clone https://github.com/rolanbadrislamov/grammar-checker-backend.git
   ```
2. **Install Dependencies**: 
   ```
   pip install -r requirements.txt
   ```
3. **Set Up OpenAI API Key**:
   Obtain an API key from OpenAI and set it as an environment variable:
   ```
   API_KEY=your-api-key
   ```
4. **Run the FastAPI Server**:
   ```
   uvicorn app.main:app --reload
   ```
   This will start the FastAPI server locally. You can access the API at `http://localhost:8000`.

5. **Docker Deployment**:
   You can also deploy the FastAPI application using Docker:
   ```
   docker build -t grammar-checker-backend .
   docker run -d -p 8000:8000 grammar-checker-backend
   ```
   This will build the Docker image and run the containerized application. You can access the API at `http://localhost:8000`.

## Design Choices

- **FastAPI**: FastAPI is chosen for its high performance, asynchronous capabilities, and easy-to-use API documentation generation.
- **OpenAI GPT-3.5 Turbo**: GPT-3.5 Turbo offers powerful language understanding capabilities suitable for grammar checking tasks.
- **API Documentation**: FastAPI automatically generates interactive API documentation using Swagger UI, making it easy for users to understand and test the API endpoints.
- **Asynchronous Processing**: To handle long-running requests without blocking the client, FastAPI utilizes asynchronous processing. This ensures that the backend remains responsive even during heavy processing.
- **Error Handling**: The application includes robust error handling mechanisms to handle various types of errors, such as API request errors, invalid input, and failures in LLM generation.
- **LLM Fault Tolerance Mechanism**: The application is designed to handle errors that may occur during LLM generation, such as syntactic errors or API failures. It includes retry mechnism to handle such errors and provide a reliable service to the users.

## Challenges and Solutions
- **Performance Optimization**: Ensuring that the application can handle long texts efficiently without causing timeouts or performance degradation required fine-tuning the asynchronous processing and optimizing API request handling.
- **Attempt to run Zephyr 7B**: Attempted to run Zephyr 7B on my own device, but it could not be run due to the lack of resources. I decided to use OpenAI GPT-3.5 Turbo instead.

## Future Improvements

- **Enhanced Error Detection**: Implementing more sophisticated error detection algorithms in addition to the LLM-based approach to improve accuracy.
- **Scalability**: Optimizing the backend for scalability to handle a large number of concurrent requests efficiently.
- **Load Balancing**: Implementing load balancing strategies to distribute incoming requests across multiple instances for improved performance. 
- **Caching**: Implementing caching mechanisms to store frequently accessed data and reduce the response time for repeated requests.
- **Testing**: Writing comprehensive unit tests and integration tests to ensure the correctness and reliability of the application.
- **Deployment**: Setting up deployment pipelines and containerization for seamless deployment to production environments.

## Conclusion

This project demonstrates the implementation of a grammar checker backend using FastAPI and OpenAI GPT-3.5 Turbo. By leveraging these technologies, the backend offers a scalable, performant, and easy-to-use solution for detecting and correcting grammatical errors in text.

Feel free to reach out if you have any questions or need further assistance! rolanbadrislamov@gmail.com

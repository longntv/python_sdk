# iogate-app-sdk-python
Python Project Skeleton

This is a Python project skeleton that provides a basic structure for developing Python applications using the Domain-Driven Design (DDD) approach. It comes with several pre-configured packages and modules that can be used to build various types of applications.
Table of Contents

    Installation
    Usage
    Project Structure
    Dependencies
    Contributing
    License

Installation

    Clone the repository: git clone https://github.com/longntv/python_sdk.git
    Change to the project directory: cd python_sdk
    Install the required packages: pip install -r requirements.txt
    Create a .env file in the project root directory and specify the required environment variables. Refer to .env.example for an example.

Usage

To run the application, simply execute the main.py file:
python main.py

This will start background worker with a Redis message queue. The application is now ready to receive and process messages.

The project consists of the following modules and packages:

    app: Contains the application code organized using the DDD approach.
    app.application: Contains the application service implementation.
    app.domain: Contains the domain model and business logic implementation.
    app.handler: Contains the message consumer implementation.
    app.infrastructure: Contains the implementation of external dependencies, such as the Redis message queue.
    app.utils: Contains utility classes and functions.

Dependencies

The project requires the following dependencies:

    dependency_injector: A lightweight dependency injection framework.
    python-dotenv: A Python package that allows you to use environment variables to configure your application.

These dependencies are listed in the requirements.txt file.

License

This project is licensed under the MIT License. See the LICENSE file for details.

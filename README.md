# Documentation for Your API

## Table of Contents
1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
    - [Create a Person](#create-a-person)
    - [Retrieve a Person](#retrieve-a-person)
    - [Update a Person](#update-a-person)
    - [Delete a Person](#delete-a-person)
3. [Known Limitations and Assumptions](#known-limitations-and-assumptions)
4. [Setting Up and Deploying](#setting-up-and-deploying)

## Introduction
This API provides CRUD operations for managing information about people. It allows you to create, retrieve, update, and delete records for individuals.

## Endpoints

### Create a Person
- **Endpoint**: `POST /api`
- **Description**: Add a new person.
- **Request Format**:
    ```json
    {
        "name": "John Doe"
    }
    ```
- **Response Format**:
    ```json
    {
        "id": 1,
        "name": "John Doe"
    }
    ```
- **Possible Errors**:
    - 400 Bad Request: If `name` is missing in the request body.
  
### Retrieve a Person
- **Endpoint**: `GET /api/<person_id>`
- **Description**: Fetch details of a person.
- **Response Format**:
    ```json
    {
        "id": 1,
        "name": "John Doe"
    }
    ```
- **Possible Errors**:
    - 404 Not Found: If person with given ID doesn't exist.

### Update a Person
- **Endpoint**: `PUT /api/<person_id>`
- **Description**: Modify details of an existing person.
- **Request Format**:
    ```json
    {
        "name": "Jane Doe"
    }
    ```
- **Response Format**:
    ```json
    {
        "message": "Person updated"
    }
    ```
- **Possible Errors**:
    - 404 Not Found: If person with given ID doesn't exist.

### Delete a Person
- **Endpoint**: `DELETE /api/<person_id>`
- **Description**: Remove a person.
- **Response Format**:
    ```json
    {
        "message": "Person deleted"
    }
    ```
- **Possible Errors**:
    - 404 Not Found: If person with given ID doesn't exist.

## Known Limitations and Assumptions
- **Limitations**:
    - This API only handles information related to a person's name.
    - It does not support authentication or authorization mechanisms.
- **Assumptions**:
    - It assumes that the client will always provide a valid person ID for retrieve, update, and delete operations.

## Setting Up and Deploying
To set up and deploy your API, follow these steps:

1. **Local Setup**:
   - Clone your repository.
   - Create a virtual environment (optional but recommended).
   - Install dependencies using `pip install -r requirements.txt`.
   - Update the database URI in `config.py` to `'sqlite:////home/yourusername/your-repo/people.db'`.
   - Run the application with `python myapp.py`.

2. **Deployment on PythonAnywhere**:
   - Log in to PythonAnywhere and open a Bash console.
   - Clone your repository with `git clone https://github.com/yourusername/your-repo.git`.
   - Create a virtual environment (optional) and install dependencies.
   - Update the database URI.
   - Run the application.
   - Access your API at `https://yourusername.pythonanywhere.com/api`.

# Flask App - User Management

This is a simple **Flask** app that implements a basic **User Management System** with RESTful API methods.

## API Methods

### 1. **GET /users**
   - **Method**: `GET`
   - **Description**: Fetches a list of all users in the system.
   - **Response**:
     - A JSON array containing all users.
   - **Example**:
     ```json
     [
       {
         "id": 1,
         "name": "Alice",
         "email": "alice@example.com"
       },
       {
         "id": 2,
         "name": "Bob",
         "email": "bob@example.com"
       }
     ]
     ```

### 2. **GET /users/<user_id>**
   - **Method**: `GET`
   - **Description**: Fetches the details of a specific user by their ID.
   - **URL Parameters**:
     - `user_id` (integer): The ID of the user.
   - **Response**:
     - A JSON object with the user details if found.
     - If not found, returns an error message.
   - **Example**:
     ```json
     {
       "id": 1,
       "name": "Alice",
       "email": "alice@example.com"
     }
     ```

### 3. **POST /users**
   - **Method**: `POST`
   - **Description**: Adds a new user to the system.
   - **Request Body**:
     - A JSON object with `name` and `email` fields.
   - **Example Request**:
     ```json
     {
       "name": "Charlie",
       "email": "charlie@example.com"
     }
     ```
   - **Response**:
     - A JSON object containing the newly created user.
   - **Example Response**:
     ```json
     {
       "id": 3,
       "name": "Charlie",
       "email": "charlie@example.com"
     }
     ```

### 4. **PUT /users/<user_id>**
   - **Method**: `PUT`
   - **Description**: Updates an existing user by their ID.
   - **URL Parameters**:
     - `user_id` (integer): The ID of the user.
   - **Request Body**:
     - A JSON object with updated `name` and/or `email` fields.
   - **Example Request**:
     ```json
     {
       "name": "Updated Name",
       "email": "updated@example.com"
     }
     ```
   - **Response**:
     - A JSON object containing the updated user details.
   - **Example Response**:
     ```json
     {
       "id": 1,
       "name": "Updated Name",
       "email": "updated@example.com"
     }
     ```

### 5. **DELETE /users/<user_id>**
   - **Method**: `DELETE`
   - **Description**: Deletes a user from the system by their ID.
   - **URL Parameters**:
     - `user_id` (integer): The ID of the user.
   - **Response**:
     - A success message indicating the user was deleted.
   - **Example Response**:
     ```json
     {
       "message": "User deleted"
     }
     ```

## What is REST API?

A **REST API** (Representational State Transfer API) is a set of rules and conventions for building and interacting with web services. REST APIs use standard HTTP methods like `GET`, `POST`, `PUT`, and `DELETE` to perform operations on resources (in this case, users). These methods correspond to operations such as retrieving, creating, updating, and deleting data.

## Testing the API with Postman

To test this Flask API using **Postman**:

1. **Download and Install Postman**:
   - If you don't have Postman, download it from [here](https://www.postman.com/downloads/).

2. **Add a Request**:
   - Open Postman and click **New**.
   - Choose **Request** and name your request.
   - Select the appropriate HTTP method (`GET`, `POST`, `PUT`, `DELETE`) from the dropdown menu.
   - Enter the API endpoint URL (e.g., `http://127.0.0.1:5000/users`).

3. **Test the Methods**:
   - For **GET** requests: Simply click **Send** to fetch the list of users or a specific user by ID.
   - For **POST** requests: Go to the **Body** tab, select **raw**, and choose **JSON**. Then, enter the new user data and click **Send** to add a new user.
   - For **PUT** requests: Enter the user ID in the URL and provide the updated data in the body.
   - For **DELETE** requests: Provide the user ID in the URL and click **Send** to delete the user.

4. **Check the Response**: The response from the Flask API will appear at the bottom of Postman, showing you either the updated data or an error message.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-app.git

# Python / FastAPI Backend Repo

## Getting Started

To get a local copy up and running, follow these steps:

1. Clone the repository.
2. (Recommended) Set up a virtual environment for isolated dependencies. See [Creating a Virtual Environment on Windows](#creating-a-virtual-environment-on-windows).
3. **Activate the virtual environment before installing dependencies or running the project.**
4. Install the required pip packages using:
   ```sh
   pip install -r requirements.txt
   ```
5. Start the development server. If you want to specify a port, use:
    ```sh
    uvicorn main:app --reload --port 8000
    ```
    If you want to use the default port (8000), simply run:
     ```sh
        uvicorn main:app --reload
    ```

## Creating a Virtual Environment on Windows

A virtual environment keeps your project dependencies isolated from your global Python installation.

To create a virtual environment:
```sh
python -m venv venv
```

To activate the virtual environment:
```sh
venv\Scripts\activate
```
**Note:**  
You must activate the virtual environment before installing dependencies or running the project. When activated, your terminal will use the isolated Python environment, ensuring packages are installed locally for this project only.

Once activated, proceed with installing dependencies and starting the server as described above.

## API Access

- **Base API Endpoint:**  
  Visit [http://localhost:8000/api](http://localhost:8000/api) to access the main API routes.

- **Interactive API Documentation (Swagger):**  
  Visit [http://localhost:8000/api/docs](http://localhost:8000/api/docs) for an interface to explore and test the API endpoints.

- **Health Check Endpoint:**  
    Visit [http://localhost:8000/api/health](http://localhost:8000/api/health) to check if the API is running.

These endpoints are available once the development server is running.

## Code Structure

The codebase is organized into several directories:

- `db`: Contains the database connection and setup files.

- `app/routers`: Contains the different routes of the application, such as test routes.
- `app/models`: Contains the data models used in the application.
- `app/schemas`: Contains the Pydantic schemas for data validation and serialization.
- `app/services`: Contains the business logic for handling different operations.
- `app/utils`: Contains utility functions.

## Environment Variables

The application uses environment variables for configuration. These are stored in a `.env` file in the root directory. Variables include:

- `POSTGRES_URL`: The full database connection URL. 

In case the full URL is not provided, the following individual parameters are used to construct the connection:

- `POSTGRES_DB`: The name of the PostgreSQL database.
- `POSTGRES_USER`: The username for the PostgreSQL database.
- `POSTGRES_PASSWORD`: The password for the PostgreSQL database.
- `POSTGRES_HOST`: The host address for the PostgreSQL database.
- `POSTGRES_PORT`: The port number for the PostgreSQL database.

Example `.env` file:
```
POSTGRES_URL="postgresql://user:password@localhost:5432/mydatabase"
POSTGRES_DB="mydatabase"
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
```

## Tech Stack

- **Backend**: Python
- **Package Management**: pip
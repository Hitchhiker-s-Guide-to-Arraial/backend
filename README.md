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
5. Start the development server.

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

## Code Structure

The codebase is organized into several directories:

- `app/routes`: Contains the different routes of the application, such as user routes.
- `app/models`: Contains the data models used in the application.
- `app/services`: Contains the business logic for handling different operations.
- `app/utils`: Contains utility functions.

## Tech Stack

- **Backend**: Python
- **Package Management**: pip
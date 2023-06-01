# DocMaker Source Code

This directory contains the source code for the DocMaker application. The application is structured in a modular way to facilitate easy expansion and maintenance.

## Directory Structure

The source code is organized as follows:

- `main.py`: This is the entry point of the application. It sets up and starts the Flask application.
- `app/`: This directory contains the core application logic.
  - `__init__.py`: Initializes the Flask application and brings together all of the various components.
  - `views.py`: Defines the routes for the Flask application.
  - `templates/`: Contains the HTML templates for the Flask application.
  - `static/`: Contains static files like CSS and JavaScript for the Flask application.
- `langchain/`: This directory contains the code related to the LangChain library.
  - `__init__.py`: Initializes the LangChain module.
  - `langchain_service.py`: Defines a class for interacting with the LangChain library.
- `utils/`: This directory contains various utility functions and classes that are used throughout the application.
  - `__init__.py`: Initializes the utils module.
  - `helpers.py`: Contains various helper functions.

## Getting Started

To run the application, you will need to have Python installed on your machine. We recommend using a virtual environment to manage your Python dependencies. Once you have Python and have set up your virtual environment, you can install the dependencies with:

```bash
pip install -r requirements.txt
```

Then, you can start the application with:

```bash
python main.py
```

This will start the Flask development server, and you can access the application at http://localhost:5000.
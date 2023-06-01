from flask import Flask
from app import create_app
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

# Create the Flask application
app = create_app()


# Run the application if this file is run directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

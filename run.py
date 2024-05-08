"""
run.py: Application Runner

This module acts as the entry point to start the Flask application using the
factory function pattern.

- Imports:
  - `create_app`: The application factory function from `app/__init__.py` that
    initializes and configures the Flask app instance.

- Variables:
  - `app`: An instance of the Flask application created via the factory function.

The module checks if it is being run as the main program and starts the Flask
development server with debugging enabled.

To run the application, execute this file directly using Python:
python run.py

"""
from app import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the Flask app on a local development server
    app.run(debug=True)

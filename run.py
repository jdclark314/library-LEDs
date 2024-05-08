from app import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the Flask app on a local development server
    app.run(debug=True)
from flask import Flask
from flask import Response

# Create an instance of the Flask class
app: Flask = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello() -> Response:
    return 'Labasss, Pasauli! Tai mano pirmoji Flask programa.'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
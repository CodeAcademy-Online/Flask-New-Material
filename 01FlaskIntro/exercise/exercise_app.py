from flask import Flask
from flask import Response

# Create an instance of the Flask class
app: Flask = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello() -> Response:
    return 'Labasss, Pasauli! Tai mano pirmoji Flask programa. As Mantas Skara :)' # Exercise 1 - Adding my name to the response

@app.route('/about')  # Exercise 3 - Adding new route
def about() -> Response:
    return 'This is the About page.'

@app.route('/contact') # Exercise 3 - Adding new route
def contact() -> Response:
    return 'Contact us at: your@email.com'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False) # Exercise 2 - Disabling debug results in a less verbose output for errors
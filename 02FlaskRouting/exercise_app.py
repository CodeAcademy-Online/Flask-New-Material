from flask import Flask

app: Flask = Flask(__name__)

@app.route('/')
def home() -> str:
    return 'Welcome to my website!'

@app.route('/about')
def about() -> str:
    return 'About Us'

@app.route('/contact')
def contact() -> str:
    return 'Contact Us'

# User profiles data
user_profiles: dict = {
    'john': {'name': 'John Doe', 'email': 'john@example.com', 'bio': 'I am a web developer.'},
    'jane': {'name': 'Jane Smith', 'email': 'jane@example.com', 'bio': 'I love hiking and photography.'}
}

# Product details data
product_details: dict = {
    '1001': {'name': 'Laptop', 'description': 'High-performance laptop', 'price': '$999'},
    '1002': {'name': 'Smartphone', 'description': 'Latest smartphone model', 'price': '$699'}
}

@app.route('/user/<username>')
def user_profile(username: str) -> str:
    if username in user_profiles:
        user_info: dict = user_profiles[username]
        return f'<h1>Welcome, {user_info["name"]}!</h1><p>Email: {user_info["email"]}</p><p>Bio: {user_info["bio"]}</p>'
    else:
        return 'User not found'

@app.route('/product/<product_id>')
def product_info(product_id: str) -> str:
    if product_id in product_details:
        product_info: dict = product_details[product_id]
        return f'<h1>Product: {product_info["name"]}</h1><p>Description: {product_info["description"]}</p><p>Price: {product_info["price"]}</p>'
    else:
        return 'Product not found'

if __name__ == '__main__':
    app.run(debug=True)

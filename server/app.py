from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Define a route that accepts a dynamic username
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run the application on port 5555 in debug mode
if __name__ == '__main__':
    app.run(port=5555, debug=True)

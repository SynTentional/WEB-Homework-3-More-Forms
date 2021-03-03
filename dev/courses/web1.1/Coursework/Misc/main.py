from flask import Flask

# create new Flask instance and assign it a root directory of the
# working file (should be named 'main.py')
app = Flask(__name__)

# routes can be created using @app.route('routeName')
# NOTE: Flask uses Python's decorater syntax so a function must
# be defined directly beneath the route declaration
@app.route('/')
def homepage():
    return "Hello, world!"

# the server can be accessed in your web browser using the URL localhost:3000/
if __name__ == '__main__':
    app.run(debug=True, port=3000)
# Why = We need to be able to create servers that fulfill requests
# 1. Utilize route variables to get data from the URL
# 2. Utilize form data collect large swaths of information at once!


# import flask library for usage!
from flask import Flask

# create an instance of the flask server
# as the root directory within 'main.py'
app = Flask(__name__)

# create some routes!
@app.route('/')
def displayHomepage():
    return "<h1>Welcome to your first website!</h1>"

@app.route('/route1')
def route1Info():
    return "<h3>congrats on making route1!</h3>"

# <> denote a route variable!
@app.route('/profile/<user_name>')
def profile(user_name):
    return "<h2>Hello " + user_name + "!<h2>"    

@app.route('/date/<month>/<day>/<year>')
def displayGiven(month, day, year):
    return f"{month} / {day} / {year}"

# creating a <form>!
formData = f"""
    <form action="/results" method="GET">
        What's your favorite pizza flavor?
        <input type="text" name="pizza_flavor>
        <br>
        What's your favorite crust type?
        <input type="text" name="crust">
        <input type="submit" value="submit pizza!">
    </form>
    """

@app.route('/formExample')
def firstForm():
    return formData

@app.route('/results', methods=['GET'])
def simple_pizza_results():
    pizza_flavor = request.args.get('pizza_flavor')
    crust = request.args.get("crust")
    return f"<h3>a {crust}-crust {pizza_flavor} pizza has been ordered!</h3>"

# turn the server on for serving!
if __name__ == "__main__":
    app.run(debug = True, port=3000)


### EVERY TIME YOU RUN FLASK YOU HAVE TO CREATE A VIRTUAL ENVIRONMENT ###
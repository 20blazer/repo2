from flask import Flask, render_template, request
from gi import get_GI
from waitress import serve 
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "BLAKE JAQUES!"
@app.route('/gi')
def get_Ginfo():
    food = request.args.get('food')
    GI_data = get_GI(food)
    return render_template(
        "gi.html",

    )

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port =8000)
from flask import Flask, render_template, request, jsonify
from gi import get_GI
from waitress import serve 
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/GI')
def get_Ginfo():
    food = request.args.get('Food')

    # check for empty strings of string with only space
    if not bool(food.strip()):
        food = "Milky Way bar"

    GI_data = get_GI(food)
    
    # #Food is not in database
    if not GI_data:
        return render_template('Food-NF.html')

    return render_template(
        "gi.html",       
        # GI_data
        title=GI_data['Food'],
        GI= f"{GI_data['GI']}",
        GL=f"{GI_data['GL']}",
        Carb=f"{GI_data['Carb']}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port =8000)
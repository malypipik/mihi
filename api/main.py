from flask import Flask
import restaurant.sps

app = Flask(__name__)

@app.route('/sps')
def homepage():
    menu = restaurant.sps.get_menu_from_sps()
    return menu

app.run(
    port=8000,
    debug=True
)
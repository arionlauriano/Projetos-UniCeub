from flask import Flask, render_template

from urls.cli_crud import bp_cli
from urls.comp_crud import bp_comp
from urls.mod_crud import bp_mod
from urls.mont_crud import bp_mont
from urls.uf_crud import bp_uf
from urls.vers_crud import bp_vers

app = Flask(__name__)
app.register_blueprint(bp_cli, url_prefix="/cli")
app.register_blueprint(bp_comp, url_prefix="/comp")
app.register_blueprint(bp_mod, url_prefix="/mod")
app.register_blueprint(bp_mont, url_prefix="/mont")
app.register_blueprint(bp_uf, url_prefix="/uf")
app.register_blueprint(bp_vers, url_prefix="/vers") 

@app.route("/")
def render_menu():
    return render_template("menu.html")

if __name__=="__main__":
    app.run(debug=True, port=900)


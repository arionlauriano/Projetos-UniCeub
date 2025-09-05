from flask import Flask, render_template
from urls.Aut_crud import bp_aut

app = Flask(__name__)
app.register_blueprint(bp_aut, url_prefix="/aut")

@app.route('/')
def index():
   return render_template('index_colec_livr.html')

if __name__ == '__main__':
   app.run(debug=True, port=9000)
